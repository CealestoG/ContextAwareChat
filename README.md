#project:
  name: "Context-Aware Chat Orchestration System"
  description: >
    A multi-agent orchestration system for intelligent and context-aware conversations. 
    It uses modular agents, coordinated through Microsoft's AutoGen framework, and supports 
    offline operation using local LLMs via Ollama. Retrieval-Augmented Generation (RAG) 
    enhances factual accuracy in responses.
--

##architecture:
  overview: |
    User Query
       │
       ▼
    QueryClassifier Agent ──► Retriever Agent ──► Domain Expert Agent
            │                          │                    │
            ▼                          ▼                    ▼
    Refinement Agent ◄──────── Response Aggregator ◄───────┘
            │
            ▼
    Final Response
--

##agents:
  - name: "QueryClassifier"
    role: "Classifies incoming queries into categories for intelligent routing."
  - name: "RetrieverAgent"
    role: "Fetches relevant documents via RAG pipeline from local vector DB."
  - name: "DomainExpertAgent"
    role: "Uses LLM to provide accurate answers based on domain-specific data."
  - name: "ResponseAggregator"
    role: "Merges responses from different agents into a cohesive reply."
  - name: "RefinementAgent"
    role: "Final pass for fluency, correctness, and clarity."
--

##tech_stack:
  languages:
    - Python 3.10+
  frameworks:
    - AutoGen
    - LangChain
  tools:
    - Ollama
    - Chroma or FAISS
  formats:
    - Markdown
    - YAML
    - JSON
--
##directory_structure: |
  context_aware_chat/
  ├── agents/
  │   ├── query_classifier.py
  │   ├── retriever_agent.py
  │   ├── domain_expert_agent.py
  │   ├── response_aggregator.py
  │   └── refinement_agent.py
  ├── rag/
  │   ├── document_loader.py
  │   ├── vector_store.py
  │   ├── retriever.py
  │   └── rag_pipeline.py
  ├── orchestration.py
  ├── llm_interface.py
  ├── README.md
  └── requirements.txt
--
##offline_capability:
  description: >
    All LLM-based processing happens locally using Ollama with models like Mistral or LLaMA3.
  benefits:
    - Privacy-preserving
    - API-key free
    - Air-gapped compatible
    - Cost-effective
--
##features:
  - Modular multi-agent architecture
  - Retrieval-Augmented Generation (RAG)
  - Local LLM integration
  - Clear separation of agent logic
  - Extensible and testable pipeline
--
##how_to_run:
  steps:
    - "Install dependencies: `pip install -r requirements.txt`"
    - "Launch Ollama with: `ollama run mistral`"
    - "Run system: `python orchestration.py`"
---
##future_improvements:
  - GUI integration using Gradio or Streamlit
  - Add persistent memory with SQLite or MongoDB
  - Multi-turn conversational history
  - Plug-and-play domain expert modules
--
##author:
  name: "CealestoG"
  purpose: "Built for research, learning, and real-world deployment."
  github: "https://github.com/CealestoG"

