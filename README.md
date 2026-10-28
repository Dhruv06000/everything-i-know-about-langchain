# Everything I Know About LangChain 🦜🔗

Welcome to my personal learning laboratory and documentation hub for **LangChain**! This repository tracks my hands-on journey as I explore the LangChain framework to upgrade and optimize my RAG (Retrieval-Augmented Generation) systems.

## 📁 Repository Structure

The codebase is organized modularly by core LangChain components:

*   **`langchain-models/`**
    *   📁 `1.llms/` — Exploring legacy text completion behaviors and foundational concepts.
    *   📁 `2.chat-models/` — Implementing modern chat APIs, including side-by-side comparative testing with OpenAI, Anthropic, and ultra-low-latency Google Gemini models.
    *   📁 `3.embedding-models/` — Studying vector representations and data preparation pipelines.

## 🛠️ Environment & Architecture

To ensure clean management, this project rejects the messy habit of splitting environments per folder. Instead, it utilizes a single, centralized workspace structure:

*   **Virtual Environment:** Sandboxed via a root-level `.venv` architecture.
*   **Secrets Management:** Protected by a local `.env` configuration (safely decoupled from Git source control).
*   **Dependency Management:** Centralized entirely within a global `requirements.txt`.

---
*Built incrementally with muscle memory, active testing, and direct application.*