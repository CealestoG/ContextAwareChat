import ollama
import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

def query_local_llm(prompt: str) -> str:
    try:
        logger.info(f"Querying LLM with {len(prompt.split())} words")
        
        response = ollama.chat(
            model='mistral',
            messages=[{
                'role': 'user',
                'content': prompt
            }],
            options={
                'temperature': 0.7,
                'num_ctx': 4096  
            }
        )
        return response['message']['content']
    except Exception as e:
        logger.error(f"LLM query failed: {e}")
        return "I encountered an error processing your request."