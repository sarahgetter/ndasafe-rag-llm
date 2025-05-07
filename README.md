# 🧠 NDA-Safe RAG App

A document-based Retrieval-Augmented Generation (RAG) application built with [Streamlit](https://streamlit.io/), [LlamaIndex](https://www.llamaindex.ai/), and [Ollama](https://ollama.com/). This prototype is designed for **local**, NDA-compliant exploration of Excel-based data using a large language model, without requiring cloud APIs or external uploads.

---

## Features

- **RAG over Excel files**: Upload `.xlsx` documents and query their contents intelligently.
- **Vector indexing**: Uses HuggingFace embeddings (`BAAI/bge-large-en-v1.5`) for efficient document retrieval.
- **Ollama local LLM**: No cloud API keys needed — runs entirely on your machine.
- **Streamlit UI**: Interactive front-end for file upload, preview, and querying.
- **Session caching**: Keeps track of file-query state for each session.

---

## Tech Stack

| Layer        | Tool                     |
| ------------ | ------------------------ |
| UI           | Streamlit                |
| LLM Backend  | Ollama (`llama3.2`)      |
| Embeddings   | HuggingFace Transformers |
| RAG Engine   | LlamaIndex               |
| File Parsing | DoclingReader            |
| Indexing     | MarkdownNodeParser       |

---

## Installation

> ⚠️ Make sure you have [Ollama](https://ollama.com/) installed and running locally.  
> This app assumes `llama3.2` is available in your Ollama models.

```bash
# Clone the repo
git clone https://github.com/sarahgetter/ndasafe-rag-llm.git
cd ndasafe-rag-llm

# (Optional) Create and activate a virtual environment
python3 -m venv venv
source venv/bin/activate

# Install dependencies
pip install -r requirements.txt
