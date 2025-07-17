from vector_store import initialize_vector_store, load_vector_store
from retriever import get_relevant_documents
from document_loader import load_documents

class RAGPipeline:
    def __init__(self, model_name="mistral", persist_dir="vectorstore"):
        self.model_name = model_name
        self.persist_dir = persist_dir
        self.vector_store = None

    def initialize(self, doc_path=None):
        if doc_path:
            docs = load_documents(doc_path)
            self.vector_store = initialize_vector_store(docs, self.model_name, self.persist_dir)
        else:
            self.vector_store = load_vector_store(self.model_name, self.persist_dir)
        return self  

    def query(self, query_text, top_k=3):
        if not self.vector_store:
            raise ValueError("Vector store not initialized. Call initialize() first.")
        return get_relevant_documents(self.vector_store, query_text, top_k=top_k)
