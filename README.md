# NDA-Safe RAG App

A privacy-conscious Retrieval-Augmented Generation (RAG) application that allows users to upload Excel spreadsheets and query their contents using a local LLM. Built with [Streamlit](https://streamlit.io/), [LlamaIndex](https://www.llamaindex.ai/), and [Ollama](https://ollama.com/).

---

## Features

- Upload `.xlsx` documents and preview them in-browser
- Extracts content using `DoclingReader` and converts to vector index
- Queries are processed with [Ollama](https://ollama.com/) using the `llama3.2` model
- Local embeddings generated using `BAAI/bge-large-en-v1.5` via Hugging Face
- Session-aware caching for efficient repeated queries
- Custom prompt template for crisp, focused answers

---

## Installation

### 1. Clone the repository

```bash
git clone https://github.com/sarahgetter/ndasafe-rag-llm.git
cd ndasafe-rag-llm
```
### 2. Create and activate a virtual environment (optional but recommended)
```bash
Copy
Edit
python -m venv .venv
source .venv/bin/activate  # On Windows: .venv\Scripts\activate
```
### 3. Install dependencies
```bash
Copy
Edit
pip install -r requirements.txt
```
Make sure the following are installed and running locally:

ollama (e.g. ollama run llama3)

System dependencies for pandas, streamlit, and Hugging Face models

## Running the App
```bash
streamlit run rag-app.py
```

## Then open the local Streamlit URL in your browser (usually http://localhost:8501).

### Usage
Upload an Excel File

Drag and drop your .xlsx file into the Streamlit app.

The contents will be previewed and indexed in-memory.

### Ask a Question

Enter a natural language query (e.g., “What are the Q4 revenue figures?”).

The model will respond using the most relevant spreadsheet context.

### Reset Chat

Use the reset button to clear session memory and reload new data.

## Project Structure
```bash
├── rag-app.py          # Main Streamlit application
├── README.md           # Project documentation
├── requirements.txt    # Python dependencies
```
## Models & Technologies Used
LLM: Ollama with llama3.2

Embeddings: BAAI/bge-large-en-v1.5

Parser: MarkdownNodeParser

Data Loader: DoclingReader for .xlsx

Framework: LlamaIndex

UI: Streamlit

## Future Enhancements
Support for other document formats (PDF, CSV)

User authentication and session persistence

Deployment via Docker or cloud (e.g., Streamlit Community Cloud, Hugging Face Spaces)

Enhanced prompt templating and feedback loop for model fine-tuning

## Example Query Prompt
vbnet
Query: What is the total number of customer complaints in Q3?

Expected Response:
Contextually retrieved and summarized information from the uploaded Excel file.


## Contributing
PRs are welcome! Please:

Fork the repo

Create a new branch (feature/my-feature)

Open a pull request describing your change

## License
MIT License — see LICENSE for details.
