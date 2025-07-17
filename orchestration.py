from query_classifier import QueryClassifier
from retriever_agent import RetrieverAgent
from domain_expert_agent import DomainExpertAgent
from response_aggregator import ResponseAggregator
from refinement_agent import RefinementAgent
from llm_interface import query_local_llm
from context_manager import ContextManager

from chat_history_db import init_db, log_message
import uuid

init_db()
session_id = str(uuid.uuid4())  

class ContextAwareChatBot:
    def __init__(self, user_id="default"):
        self.query_classifier = QueryClassifier()
        self.retriever = RetrieverAgent()
        self.domain_expert = DomainExpertAgent()
        self.aggregator = ResponseAggregator()
        self.refiner = RefinementAgent()
        self.context = ContextManager()
        self.user_id = user_id
    
    def chat(self, user_query: str) -> str:
        try:
           
            self.context.add_to_history("user", user_query)
            log_message(session_id, "user", user_query)  
            
            
            context_prompt = self.context.get_context_prompt()
            full_query = f"{context_prompt}\n\nCurrent Query: {user_query}"
            
            
            query_type = self.query_classifier.classify(full_query)
            log_message(session_id, "QueryClassifier", query_type) 

            relevant_docs = self.retriever.retrieve(query_type, full_query)
            log_message(session_id, "RetrieverAgent", f"Retrieved {len(relevant_docs)} documents")  
            
            if not relevant_docs:
                response = query_local_llm(full_query)
                log_message(session_id, "LLM", response)  
            else:
                response = self.domain_expert.generate_response(
                    query=full_query,
                    documents=relevant_docs
                )
                log_message(session_id, "DomainExpertAgent", response)  
            
            refined = self.refiner.refine(response)
            log_message(session_id, "RefinementAgent", refined)  
            
            self.context.add_to_history("assistant", refined)
            
            return refined
        except Exception as e:
            return f" System error: {str(e)}. Please try again."
    
    def reset_context(self):
        self.context.clear_history()
