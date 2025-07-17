from autogen import AssistantAgent
from rag_pipeline import RAGPipeline
from typing import List, Dict, Any
import warnings

class RetrieverAgent:
    def __init__(self, name: str = "Retriever"):
        self.agent = AssistantAgent(name=name)
        self.rag = RAGPipeline()
        try:
            self.rag.initialize("docs/")
        except Exception as e:
            warnings.warn(f"Failed to initialize RAG pipeline: {e}")
            self.rag.initialize()

    def retrieve(self, query_type: str, full_context: str) -> List[Dict[str, Any]]:
        if not full_context.strip():
            return []
        
        keywords = " ".join(full_context.split()[-20:])
        
        try:
            results = self.rag.query(keywords)
            return [{
                "content": doc.page_content,
                "metadata": doc.metadata
            } for doc in results]
        except Exception as e:
            warnings.warn(f"Retrieval failed: {e}")
            return []