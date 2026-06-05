# 📚 Research Paper RAG Chatbot

## Overview

The Research Paper RAG Chatbot is an AI-powered application that enables users to upload one or more research papers in PDF format and interact with them through natural language questions.

Instead of relying solely on the knowledge of a Large Language Model (LLM), this chatbot uses a Retrieval-Augmented Generation (RAG) architecture. It retrieves relevant information from the uploaded research papers and generates accurate, context-aware responses based on the retrieved content.

This project is built using:

* Python
* Streamlit
* LangChain
* Google Gemini
* FAISS Vector Database
* PyPDF

---

## Features

### Research Paper Question Answering

Users can ask questions about uploaded research papers and receive context-aware answers.

### Multiple PDF Support

Upload and process multiple research papers simultaneously.

### Semantic Search

Uses vector embeddings to retrieve the most relevant content from research papers.

### Context-Based Responses

Answers are generated only from the uploaded documents.

### Fast Retrieval

FAISS vector database enables efficient similarity search.

### User-Friendly Interface

Built with Streamlit for a simple and interactive experience.

---

## Tech Stack

| Component              | Technology                      |
| ---------------------- | ------------------------------- |
| Frontend               | Streamlit                       |
| LLM                    | Gemini 2.0 Flash                |
| Framework              | LangChain                       |
| Embeddings             | Google Generative AI Embeddings |
| Vector Database        | FAISS                           |
| PDF Processing         | PyPDF                           |
| Environment Management | Python Dotenv                   |

---

## Project Structure

```text
Research_Paper_RAG/
│
├── app.py
├── requirements.txt
├── .env
├── README.md
│
├── src/
│   ├── pdf_loader.py
│   ├── text_splitter.py
│   ├── vector_store.py
│   ├── rag_chain.py
│   └── prompt.py
│
├── faiss_index/
│
└── venv/
```

---

## Prerequisites

Before running the project, ensure that the following software is installed:

### Python

Recommended Version:

```text
Python 3.11+
```

Verify Installation:

```bash
python --version
```

### Git

Verify Installation:

```bash
git --version
```

---

## Installation Steps

### Clone the Repository

```bash
git clone <repository-url>
```

Navigate to the project directory:

```bash
cd Research_Paper_RAG
```

---

### Create Virtual Environment

```bash
python -m venv venv
```

Activate the virtual environment:

#### Windows

```bash
venv\Scripts\activate
```

#### Linux / macOS

```bash
source venv/bin/activate
```

---

### Install Required Packages

Install all dependencies:

```bash
pip install -r requirements.txt
```

Alternatively:

```bash
pip install streamlit langchain langchain-community langchain-google-genai faiss-cpu pypdf python-dotenv
```

---

## Gemini API Configuration

Generate an API key from Google AI Studio:

https://aistudio.google.com

Create a `.env` file in the project root directory:

```env
GOOGLE_API_KEY=YOUR_GEMINI_API_KEY
```

Example:

```env
GOOGLE_API_KEY=AIzaSyXXXXXXXXXXXXXXXXXXXX
```

---

## Running the Application

Start the Streamlit application:

```bash
streamlit run app.py
```

After execution, Streamlit will provide a local URL:

```text
http://localhost:8501
```

Open the URL in your browser.

---

## Workflow of the Chatbot

### Step 1: Upload Research Papers

The user uploads one or more PDF research papers.

↓

### Step 2: PDF Extraction

The chatbot extracts textual content from each uploaded PDF using PyPDFLoader.

↓

### Step 3: Text Chunking

Large documents are divided into smaller chunks using LangChain's Recursive Character Text Splitter.

↓

### Step 4: Embedding Generation

Each chunk is converted into a numerical vector representation using Google Generative AI Embeddings.

↓

### Step 5: Vector Storage

The embeddings are stored in a FAISS vector database.

↓

### Step 6: User Question

The user submits a natural language query.

Example:

```text
What methodology was used in this research paper?
```

↓

### Step 7: Similarity Search

FAISS retrieves the most relevant chunks related to the user's question.

↓

### Step 8: Context Construction

Relevant chunks are assembled into a context block.

↓

### Step 9: Gemini Response Generation

The retrieved context and user query are sent to Gemini.

↓

### Step 10: Final Answer

Gemini generates an answer grounded in the uploaded research papers.

---

## RAG Architecture

```text
Research Papers (PDF)
          │
          ▼
     PDF Loader
          │
          ▼
    Text Splitter
          │
          ▼
      Chunks
          │
          ▼
     Embeddings
          │
          ▼
   FAISS Vector DB
          │
          ▼
      Retriever
          │
          ▼
      LangChain
          │
          ▼
   Gemini 2.0 Flash
          │
          ▼
   Final Response
```

---

## Sample Questions

Users can ask questions such as:

```text
What is the objective of this paper?

Summarize the methodology section.

What datasets were used?

What are the key findings?

What limitations are mentioned?

What future work is proposed?

Compare the approaches discussed in the uploaded papers.
```

---

## Future Enhancements

* Conversation Memory
* Research Paper Summarization
* Multi-Paper Comparison
* Citation Generation
* Research Gap Analysis
* Hybrid Search (FAISS + BM25)
* Cloud Vector Database Integration
* User Authentication
* Chat History Storage
* Deployment on AWS / Azure / GCP

---

## Learning Outcomes

This project demonstrates:

* Retrieval-Augmented Generation (RAG)
* LangChain Framework
* Prompt Engineering
* Vector Databases
* Semantic Search
* Embedding Models
* Large Language Model Integration
* Streamlit Application Development
* Research Paper Analysis

---

## Author

Developed as a practical implementation of a Research Paper Question Answering System using LangChain, Gemini, and FAISS.
