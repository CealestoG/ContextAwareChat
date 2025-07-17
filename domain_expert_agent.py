from autogen.agentchat import AssistantAgent  # ADD THIS IMPORT
from typing import List, Dict
from llm_interface import query_local_llm

class DomainExpertAgent:
    def __init__(self):
        self.agent = AssistantAgent(name="DomainExpert")  # Now properly defined
    def generate_response(self, query: str, documents: List[Dict]) -> str:
        if not documents:
            return query_local_llm(f"Answer without context: {query}")

        knowledge = "\n---\n".join([doc["content"] for doc in documents[:3]])
        
        
        prompt = (
            "You are an expert assistant. Answer the query using the provided context.\n\n"
            f"CONTEXT:\n{query}\n\n"
            f"KNOWLEDGE BASE:\n{knowledge}\n\n"
            "Provide a detailed, accurate response:"
        )
        
        return query_local_llm(prompt)