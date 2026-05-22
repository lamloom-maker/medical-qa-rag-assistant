#  Medical QA Assistant - RAG System

> Production-ready medical question-answering system using Retrieval-Augmented Generation (RAG) on verified NIH medical sources.

##  Live Demo

**Try it now:** [https://huggingface.co/spaces/Lamloom/medical-qa-assistant](https://huggingface.co/spaces/Lamloom/medical-qa-assistant)

##  Project Overview

An AI-powered medical assistant that provides accurate, source-cited answers to medical questions using:
- **1,500+ verified Q&A pairs** from NIH sources (MedQuAD)
- **RAG architecture** to prevent LLM hallucinations
- **Citation system** for every answer

##  Key Features

- ✅ Semantic search across medical knowledge base
- ✅ Source citation for every answer
- ✅ **Hallucination prevention** — only answers from verified sources
- ✅ Recognizes when it lacks sufficient information instead of fabricating
- ✅ Medical disclaimer on all responses

##  Tech Stack

| Component | Technology |
|-----------|-----------|
| Language | Python 3.10+ |
| Vector Database | ChromaDB |
| Embeddings | Sentence-Transformers (all-MiniLM-L6-v2) |
| LLM | Google Gemini 2.5 Flash |
| UI | Streamlit |
| Deployment | Hugging Face Spaces |

##  How It Works

1. User asks a medical question
2. The question is converted to an embedding vector
3. ChromaDB searches 1,500+ Q&A pairs for the most relevant matches
4. Top matches are sent to Gemini as verified context
5. Gemini generates a unified, source-cited answer

##  Dataset

**MedQuAD** — Medical Question Answering Dataset
- Source: National Institutes of Health (NIH)
- 47,457 Q&A pairs from 12 medical sources

##  Project Structure

- `medical_rag_system.py` — Core RAG system class
- `01_data_exploration.ipynb` — Data processing & EDA
- `02_vector_database.ipynb` — Embeddings & ChromaDB setup
- `DATA_SETUP.md` — Dataset setup guide

##  Data Visualizations

The project includes EDA visualizations:
- Source distribution across medical databases
- Question type analysis
- Question/answer length distributions

##  Author

**Lama Turki**
- GitHub: [@lamloom-maker](https://github.com/lamloom-maker)

##  License

MIT License
