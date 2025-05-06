import os
import gc
import tempfile
import uuid
import pandas as pd
import streamlit as st

from llama_index.core import Settings, PromptTemplate, VectorStoreIndex, SimpleDirectoryReader
from llama_index.llms.ollama import Ollama
from llama_index.embeddings.huggingface import HuggingFaceEmbedding
from llama_index.readers.docling import DoclingReader
from llama_index.core.node_parser import MarkdownNodeParser

# === Session Initialization ===
if "id" not in st.session_state:
    st.session_state.id = uuid.uuid4()
    st.session_state.file_cache = {}

session_id = st.session_state.id


@st.cache_resource
def load_llm():
    """Load the Ollama LLM with a 120 second timeout."""
    return Ollama(model="llama3.2", request_timeout=120.0)


@st.cache_data
def read_excel(file):
    """Read and cache Excel file as a DataFrame."""
    return pd.read_excel(file)


def display_excel(file):
    """Display Excel contents."""
    st.markdown("### Excel Preview")
    df = read_excel(file)
    st.dataframe(df)


def reset_chat():
    """Reset the Streamlit session state for chat."""
    st.session_state.messages = []
    st.session_state.context = None
    gc.collect()


def build_query_engine(temp_dir, file_key):
    """
    Process uploaded Excel file and build a query engine for RAG.
    Stores the result in st.session_state.file_cache.
    """
    reader = DoclingReader()
    loader = SimpleDirectoryReader(
        input_dir=temp_dir,
        file_extractor={".xlsx": reader}
    )

    docs = loader.load_data()

    # Load models
    llm = load_llm()
    embed_model = HuggingFaceEmbedding(
        model_name="BAAI/bge-large-en-v1.5", trust_remote_code=True)

    Settings.embed_model = embed_model
    Settings.llm = llm

    node_parser = MarkdownNodeParser()
    index = VectorStoreIndex.from_documents(
        documents=docs,
        transformations=[node_parser],
        show_progress=True
    )

    query_engine = index.as_query_engine(streaming=True)

    # Prompt customization
    qa_prompt_tmpl_str = (
        "Context information is below.\n"
        "---------------------\n"
        "{context_str}\n"
        "---------------------\n"
        "Given the context information above I want you to think step by step to answer the query in a highly precise and crisp manner focused on the final answer. "
        "In case you don't know the answer say 'I don't know!'.\n"
        "Query: {query_str}\n"
        "Answer: "
    )
    qa_prompt_tmpl = PromptTemplate(qa_prompt_tmpl_str)

    query_engine.update_prompts({
        "response_synthesizer:text_qa_template": qa_prompt_tmpl
    })

    st.session_state.file_cache[file_key] = query_engine
    return query_engine
