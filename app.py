import os
from dotenv import load_dotenv

# Force override system variables with .env file
load_dotenv(override=True)

import streamlit as st
import fitz  # pymupdf
import time
import re
import traceback

# Internal Modules
from src.arena import Arena
from src.judge import Judge
from src.selector import Selector

# --- PAGE CONFIGURATION ---
st.set_page_config(
    page_title="Bull vs Bear Arena",
    page_icon="⚖️",
    layout="wide"
)

# --- HEADER ---
st.title("⚖️ Long/Short Arena (Deep Reasoning)")
st.markdown("""
**Institutional AI Duel:** 1. **Upload** research documents.
2. **AI Selector** identifies the trade target.
3. **Adjudicate:** Long and Short PMs debate the evidence, revealing their step-by-step reasoning.
""")
st.divider()

# --- HELPER: TICKER GUESSING ---
def guess_ticker_from_files(file_list):
    """
    Scans filenames for patterns like 'CRWV.pdf', 'CRWV_Report.pdf', or '(CRWV)'.
    """
    for f in file_list:
        name = f.name
        # Pattern 1: Ticker in parens -> (CRWV)
        match = re.search(r"\(([A-Za-z]{2,5})\)", name)
        if match: return match.group(1).upper()
        
        # Pattern 2: Starts with Ticker -> CRWV_Report.pdf or CRWV.pdf
        match_start = re.match(r"^([A-Z]{2,5})[\W_.]", name)
        if match_start: return match_start.group(1).upper()

    return None

# --- SIDEBAR: CONTROLS ---
with st.sidebar:
    st.header("1. Input Data")
    
    uploaded_files = st.file_uploader(
        "Upload Documents (PDF)", 
        type=["pdf"], 
        accept_multiple_files=True
    )
    
    st.info("💡 **Tip:** Uploading multiple large files may take 10-20 seconds to process.")

    # --- STATE MANAGEMENT ---
    if "arena" not in st.session_state: st.session_state.arena = Arena()
    if "selector" not in st.session_state: st.session_state.selector = Selector()
    if "target_cache" not in st.session_state: st.session_state.target_cache = None
    if "raw_text_cache" not in st.session_state: st.session_state.raw_text_cache = None
    
    if st.button("Reset All"):
        st.session_state.arena = Arena()
        st.session_state.selector = Selector()
        st.session_state.target_cache = None
        st.session_state.raw_text_cache = None
        st.rerun()

@st.cache_data(show_spinner=False)
def extract_text_from_files(uploaded_files):
    combined_text = ""
    TIMEOUT_SECONDS = 120
    start_time = time.time()
    
    progress_bar = st.progress(0)
    status_text = st.empty()
    
    total_files = len(uploaded_files)
    timed_out = False

    for file_index, uploaded_file in enumerate(uploaded_files):
        if timed_out: break

        status_text.text(f"Processing {uploaded_file.name}...")
        bytes_data = uploaded_file.getvalue()
        
        try:
            with fitz.open(stream=bytes_data, filetype="pdf") as doc:
                for page_num, page in enumerate(doc):
                    if time.time() - start_time > TIMEOUT_SECONDS:
                        st.error(f"⚠️ Extraction timed out. Partial data loaded.")
                        timed_out = True
                        break
                    
                    combined_text += page.get_text(sort=True) + "\n\n"
        
        except Exception as e:
            st.error(f"Error reading {uploaded_file.name}: {e}")

        progress_bar.progress((file_index + 1) / total_files)

    if not timed_out:
        status_text.text("Extraction complete!")
        time.sleep(0.5)
    
    status_text.empty()
    progress_bar.empty()
    
    return combined_text

# --- MAIN DASHBOARD LOGIC ---
if uploaded_files:
    
    # STEP 0: TEXT EXTRACTION
    if st.session_state.raw_text_cache is None:
        with st.spinner("📄 Extracting text from PDFs..."):
            text = extract_text_from_files(uploaded_files)
            st.session_state.raw_text_cache = text
            st.success(f"Extracted {len(text)} characters.")
    
    raw_text = st.session_state.raw_text_cache

    if raw_text:
        # STEP 1: AUTO-SELECTION
        if st.session_state.target_cache is None:
            with st.spinner("🔍 AI Analyst is identifying the best trading vehicle..."):
                try:
                    selection = st.session_state.selector.select_target(raw_text[:30000])
                    st.session_state.target_cache = selection 
                except Exception as e:
                    print(f"Selector Error: {e}") 
        
        sel = st.session_state.target_cache
        
        # Display Selection
        with st.expander("🎯 Target Confirmation", expanded=True):
            col_type, col_ticker, col_reason = st.columns([1, 1, 3])
            
            # --- INTELLIGENT DEFAULT LOGIC ---
            ai_ticker = sel.primary_ticker if sel else None
            filename_ticker = guess_ticker_from_files(uploaded_files)
            
            # Determine the source of the ticker
            if ai_ticker and ai_ticker != "SPY":
                final_ticker = ai_ticker
                final_reasoning = sel.reasoning
                source_label = "AI Analysis"
            elif filename_ticker:
                final_ticker = filename_ticker
                final_reasoning = f"⚡ **Auto-detected from filename:** '{uploaded_files[0].name}' indicates {filename_ticker} is the primary target."
                source_label = "Filename Scan"
            else:
                final_ticker = "SPY"
                final_reasoning = "Could not detect specific ticker. Defaulting to Market (SPY)."
                source_label = "Default"

            with col_type:
                # If we don't have an AI selection object, guess Single Stock
                is_sector = sel.is_sector_report if sel else False
                report_type = "🏗️ Sector/Macro" if is_sector else "🏢 Single Stock"
                st.info(f"**Type:** {report_type}")
            
            with col_ticker:
                ticker_input = st.text_input("Trading Ticker", value=final_ticker)
            
            with col_reason:
                st.caption(f"Source: {source_label}")
                st.write(final_reasoning)

        # STEP 2: THE ADJUDICATION
        if st.button(f"⚖️ ADJUDICATE: {ticker_input}", type="primary", use_container_width=True):
            
            status_container = st.empty()
            
            try:
                # --- PHASE 1: PM DEBATE ---
                status_container.info(f"🧠 Phase 1: Long and Short PMs are performing deep reasoning on {ticker_input}...")
                
                long_res, short_res = st.session_state.arena.fight(raw_text[:60000], target=ticker_input)
                
                # =========================================================
                # 🛡️ CIRCUIT BREAKER: Stop here if AI failed
                # =========================================================
                if long_res is None or short_res is None:
                    status_container.empty()
                    st.error("🚨 **AI Agents Failed:** The Long/Short PMs returned empty results.")
                    st.warning("👉 **Action:** Check your `.env` file. Your OpenAI API Key is likely invalid or missing.")
                    st.stop()
                # =========================================================
                
                # --- PHASE 2: CIO JUDGMENT ---
                status_container.info("⚖️ Phase 2: The CIO is weighing the evidence...")
                judge = Judge()
                verdict = judge.adjudicate(long_res, short_res)
                
                status_container.empty()

                # SECTION 1: THE VERDICT
                st.markdown(f"### 🏛️ Final Verdict: {ticker_input}")
                
                winner = verdict.winner if verdict else "Undecided"
                
                if "Long" in winner:
                    theme_color, winner_icon = "green", "🔵"
                elif "Short" in winner:
                    theme_color, winner_icon = "red", "🔴"
                else:
                    theme_color, winner_icon = "gray", "⚪"

                with st.container(border=True):
                    kpi1, kpi2, kpi3 = st.columns([1, 2, 2])
                    with kpi1:
                        net_risk = verdict.net_risk_units if verdict else 0
                        st.metric("Net Risk Units", f"{net_risk:+.1f}")
                    with kpi2:
                        st.caption("Winner")
                        st.subheader(f":{theme_color}[{winner_icon} {winner}]")
                    with kpi3:
                        st.caption("Deciding Factor")
                        factor = verdict.deciding_factor if verdict else "Insufficient Data"
                        st.write(f"**{factor}**")

                    st.divider()
                    if verdict:
                        st.markdown(f"**Executive Summary:** {verdict.executive_summary}")

                # SECTION 2: THE DEEP REASONING
                st.markdown("---")
                st.subheader("🧠 The Analytical Debate")
                st.markdown("Review the step-by-step reasoning trace of how each PM arrived at their conviction.")

                col1, col2 = st.columns(2)
                
                # --- LONG SIDE ---
                with col1:
                    st.header("🔵 Bull Case")
                    if long_res:
                        with st.container(border=True):
                            st.caption("Reasoning Trace")
                            st.markdown(f"*{long_res.analytical_process}*")
                            st.divider()
                            if hasattr(long_res, 'risk_sizing') and long_res.risk_sizing:
                                st.metric("Risk Allocated", f"{long_res.risk_sizing.risk_units}/10")
                                st.write(f"**Role:** {long_res.risk_sizing.role_in_book}")
                            else:
                                st.warning("No risk sizing generated.")

                # --- SHORT SIDE ---
                with col2:
                    st.header("🔴 Bear Case")
                    if short_res:
                        with st.container(border=True):
                            st.caption("Reasoning Trace")
                            st.markdown(f"*{short_res.analytical_process}*")
                            st.divider()
                            if hasattr(short_res, 'risk_sizing') and short_res.risk_sizing:
                                st.metric("Risk Allocated", f"{short_res.risk_sizing.risk_units}/10")
                                st.write(f"**Role:** {short_res.risk_sizing.role_in_book}")
                            else:
                                st.warning("No risk sizing generated.")

                # SECTION 3: CONVICTION LEVERS
                st.markdown("### 🎚️ Conviction Levers")
                st.write("The specific arguments that tipped the scale.")
                
                lever_col1, lever_col2 = st.columns(2)
                
                with lever_col1:
                    st.subheader("🐂 Top Upside Drivers")
                    if long_res and hasattr(long_res, 'key_arguments'):
                        for i, arg in enumerate(long_res.key_arguments):
                            st.info(f"{i+1}. {str(arg)}")
                    else:
                        st.caption("No specific upside levers listed.")

                with lever_col2:
                    st.subheader("🐻 Top Downside Risks")
                    if short_res and hasattr(short_res, 'key_arguments'):
                        for i, arg in enumerate(short_res.key_arguments):
                            st.warning(f"{i+1}. {str(arg)}")
                    else:
                        st.caption("No specific downside risks listed.")

                # SECTION 4: PRE-MORTEM
                if verdict and hasattr(verdict, 'pre_mortem'):
                    st.divider()
                    with st.expander("☠️ Pre-Mortem: What Kills This Thesis?", expanded=False):
                        st.markdown(verdict.pre_mortem)

            except Exception as e:
                st.error("An error occurred during adjudication.")
                st.code(traceback.format_exc())

    # --- DEBUG SECTION ---
    with st.expander("🕵️ Debug: View Raw Text"):
        st.write(raw_text[:5000])