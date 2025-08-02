# Context-Aware Chat Orchestration System

A multi-agent orchestration system for intelligent and context-aware conversations.  
It uses modular agents, coordinated through Microsoft's AutoGen framework, and supports offline operation using local LLMs via Ollama.  
Retrieval-Augmented Generation (RAG) enhances factual accuracy in responses.

---

## 🧩 Agents

| Agent              | Role                                                                 |
|--------------------|----------------------------------------------------------------------|
| QueryClassifier     | Classifies incoming queries into categories for intelligent routing |
| RetrieverAgent      | Fetches relevant documents via RAG pipeline from local vector DB    |
| DomainExpertAgent   | Uses LLM to provide domain-specific answers                         |
| ResponseAggregator  | Merges responses from different agents into a cohesive reply        |
| RefinementAgent     | Final pass for fluency, correctness, and clarity                    |

---

## 🛠️ Tech Stack

- **Languages:** Python 3.10+
- **Frameworks:** AutoGen, LangChain
- **Tools:** Ollama, Chroma or FAISS
- **Formats:** Markdown, YAML, JSON

---
##  Offline Capability

All LLM-based processing happens locally using Ollama with models like Mistral or LLaMA3.

**Benefits:**
- Privacy-preserving  
- API-key free  
- Air-gapped compatible  
- Cost-effective  

---

##  Features

- Modular multi-agent architecture  
- Retrieval-Augmented Generation (RAG)  
- Local LLM integration  
- Clear separation of agent logic  
- Extensible and testable pipeline  

---

##  How to Run

1. Install dependencies:  
2. ollama run mistral
3.python orchestration.py
---
## 🧭 Future Improvements

- GUI integration using Gradio or Streamlit  
- Add persistent memory with SQLite or MongoDB  
- Multi-turn conversational history  
- Plug-and-play domain expert modules  

---

## 👨‍💻 Author

**CealestoG**  
Built for research, learning, and real-world deployment.  
GitHub: [https://github.com/CealestoG](https://github.com/CealestoG)

