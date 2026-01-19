# AI Flow Studio – Retrieval Augmented Generation Workflow Engine
## 📌 Overview
AI Flow Studio is a visual AI workflow orchestration platform designed to build **Retrieval-Augmented Generation (RAG)** pipelines. It allows users to transform static documents into interactive knowledge bases by combining vector embeddings with Large Language Models (LLMs).


---

## 🚀 Key Features

* **Visual Workflow Builder:** Drag-and-drop interface powered by React Flow.
* **End-to-End RAG Pipeline:** Integrated PDF uploading, text chunking, and vector storage.
* **Vector Search:** Semantic retrieval using ChromaDB and Sentence Transformers.
* **Contextual AI:** Leverages Google Gemini to answer questions based strictly on provided data.
* **Hybrid Storage:** PostgreSQL for relational data (workflows/logs) and ChromaDB for embeddings.
* **Secure Auth:** Supabase-managed authentication with JWT validation.
* **Dockerized:** Seamless deployment using Docker Compose.

---

## 🏗️ High-Level Architecture

The system follows a modular flow to process queries:

1.  **User Query:** Triggered via the Workflow UI.
2.  **Workflow Engine:** Orchestrates the node-to-node execution logic.
3.  **Knowledge Base Node:** Fetches relevant context from the Vector Store.
4.  **Vector Similarity Search:** Matches query embeddings against stored document chunks.
5.  **LLM with Context:** Gemini generates a response using the retrieved "Ground Truth."
6.  **Persistence:** Answers are logged to PostgreSQL for history.

---

## 🛠️ Tech Stack

| Layer | Technologies |
| :--- | :--- |
| **Frontend** | React, Vite, Tailwind CSS, React Flow, Supabase JS |
| **Backend** | FastAPI, SQLAlchemy, PyMuPDF, Sentence Transformers |
| **LLM** | Google Gemini API |
| **Databases** | PostgreSQL (Relational), ChromaDB (Vector Store) |
| **DevOps** | Docker, Docker Compose |

---

## 📂 Project Structure

```text
├── backend/
│   ├── db/            # Database configurations
│   ├── models/        # SQLAlchemy & Pydantic models
│   ├── routers/       # API endpoints (Auth, Workflow, RAG)
│   ├── services/      # Business logic (Embedding, LLM, Chunking)
│   └── utils/         # Helper functions
├── frontend/
│   ├── components/    # React Flow nodes & UI elements
│   ├── pages/         # Dashboard & Auth views
│   ├── lib/           # Supabase & API clients
│   └── types/         # TypeScript definitions
└── docker-compose.yml
```

---
## ⚙️ Setup & Installation
**1. Environment Variables**

Create a .env file in the backend folder:
Code snippet
```
DATABASE_URL=postgresql://user:password@db:5432/aiflow
SUPABASE_URL=your_supabase_url
SUPABASE_SERVICE_ROLE_KEY=your_key
GEMINI_API_KEY=your_gemini_api_key
```
Create a .env file in the frontend folder:

Code snippet
```
VITE_SUPABASE_URL=your_supabase_url
VITE_SUPABASE_ANON_KEY=your_anon_key

```
**2. Run with Docker**
Launch the entire stack (Frontend, Backend, Postgres, ChromaDB) with one command:

```
docker compose up --build
```
Frontend: http://localhost:5173

Backend: http://localhost:8000

---
## 🧬 RAG Pipeline Logic
Ingestion: PDF text is extracted and split into chunks with defined overlap to maintain context.

Embedding: Sentence-Transformers convert text chunks into high-dimensional vectors.

Retrieval: When a user asks a question, the query is embedded and a Top-K similarity search is performed in ChromaDB.

Generation: The retrieved chunks are injected into the Gemini prompt as a "Context" block to prevent hallucinations.

---
## 👤 Author
Vishnu Vamsi

Email: vishnuvamsi04@gmail.com
