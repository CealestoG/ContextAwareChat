from langchain_chroma import Chroma  
from langchain_ollama.embeddings import OllamaEmbeddings
from langchain_text_splitters import CharacterTextSplitter
from langchain_community.document_loaders import TextLoader
import os

persist_directory = "vectorstore"

def initialize_vector_store(docs, embedding_model_name="mistral", persist_dir=persist_directory):
    embeddings = OllamaEmbeddings(model=embedding_model_name)

    
    test_embedding = embeddings.embed_query("test")
    if len(test_embedding) != 4096:
        raise ValueError(f"Expected embedding dimension of 4096, got {len(test_embedding)}")

    
    if os.path.exists(persist_dir):
        import shutil
        shutil.rmtree(persist_dir)

    vector_store = Chroma.from_documents(
        documents=docs,
        embedding=embeddings,
        persist_directory=persist_dir
    )
    return vector_store

def load_vector_store(embedding_model_name="mistral", persist_dir=persist_directory):
    embeddings = OllamaEmbeddings(model=embedding_model_name)
    return Chroma(persist_directory=persist_dir, embedding_function=embeddings)
