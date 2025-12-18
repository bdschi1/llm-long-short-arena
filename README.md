# ⚖️ Institutional Long/Short Arena

An autonomous multi-agent system that simulates an institutional investment debate. Two AI agents (Long PM and Short PM) analyze uploaded research documents, conduct deep reasoning debates, and a third AI (CIO/Judge) renders a final verdict with risk sizing.

## 🌟 Key Features

* **📄 PDF Ingestion:** Upload raw research reports (10K, Earnings Call, Sell-side Research).
* **🤖 Auto-Targeting:** The "Analyst" agent automatically identifies the ticker.
    * *Fallback:* If the AI is unsure, it intelligently scans filenames (e.g., `CRWV_Report.pdf`) to detect the target.
* **🧠 Deep Reasoning:** The Bull and Bear agents do not just summarize; they perform step-by-step chain-of-thought reasoning to find non-obvious drivers.
* **⚖️ The CIO Verdict:** A final adjudicator weighs the arguments and assigns a **Net Risk Unit** score (-10 to +10).

## 🚀 Quick Start

### 1. Prerequisites
* Python 3.10+
* OpenAI API Key

### 2. Installation
```bash
git clone [https://github.com/YOUR_USERNAME/llm-long-short-arena.git](https://github.com/YOUR_USERNAME/llm-long-short-arena.git)
cd llm-long-short-arena
pip install -r requirements.txt