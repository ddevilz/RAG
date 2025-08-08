# RAG

🚀 Overview
RAG API enables users to submit document URLs (PDF, DOCX, Emails) and questions, returning context-grounded answers using powerful language models. It combines semantic document search (FAISS + embeddings) with LLM-driven answer generation through LangChain.

📋 Features
- Accepts multiple document URLs (PDF, DOCX, Email formats)

- On-the-fly text extraction, chunking, and semantic indexing

- Embeddings via OpenAI; fast vector search via FAISS

- LLM (ChatGPT or compatible) for Q&A with context support

- API-key secured endpoints

- Designed for cloud/on-prem, containerization ready

- Modular: easy to extend with new document types, models, or vector store backends

🏗️ Architecture & Data Flow

text
            
      |  API User | -----> | Document Download| -----> | Text Extraction |        
             
                                                                |
                                                      
                                                          Text Chunking    
                                                   
                                                                |          
                                                          
                                                            |Embedding|
                                                            
                                                                |
                                                     
                                                        |    FAISS Vector Store |
                                                        
                                                                |
                                                    
                                                        | Semantic Similarity Retrieval |
                                                      
                                                                |
                                                      
                                                        |     LLM Answering      |
                                                       
                                                               |
                                                        
                                                        |   API Response     |
                                                       
Step-by-step:

* Request: User posts document URLs and questions

* Download: URLs fetched, file type identified and saved

* Extraction: Document content parsed into raw text

* Chunking: Text split into overlapping, semantic chunks

* Embedding: Chunks embedded with OpenAI API

* Indexing: FAISS stores and indexes embeddings for fast retrieval

* Questioning: Nearest chunks per question passed as context to LLM

* Response: LLM-generated answers returned to the API user

🛠️ Tech Stack
    Layer	          Tech
    Cloud	          Vendor-agnostic, deploy anywhere
    Backend	Python    (FastAPI), Pydantic, Uvicorn, Docker
    Document Proc	  Requests, LangChain loaders
    Vector Store	  FAISS, OpenAI API for embeddings
    LLM	OpenAI        (ChatGPT, GPT-4 via LangChain)
    Security	      Header-based API Key Auth
    Config Mgmt	      .env + Pydantic Settings
    Frontend	      Not included (API-first, UI pluggable)

⚡ Quickstart
1. Clone & Install
    bash
    git clone https://github.com/your-org/rag-api.git
    cd rag-api
    pip install -r requirements.txt
2. Environment Setup
    Add a .env with:

    text
    API_KEY=your-own-api-key
    OPENAI_API_KEY=sk-...
    OPENAI_API_BASE=https://api.openai.com/v1
    OPENAI_API_VERSION=2023-05-15
    FAISS_INDEX_PATH=faiss_index
    DOCUMENTS_PATH=documents
    DOCUMENT_STORAGE_PATH=document_storage

3. API Usage
    /api/v1/hackrx/run (POST): Submit documents (single/multiple URLs) and questions (list)

    Returns: List of Q&A answers    
