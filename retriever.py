from langchain_community.vectorstores import Chroma

def get_relevant_documents(vector_store, query, top_k=3):
    return vector_store.similarity_search(query, k=top_k)