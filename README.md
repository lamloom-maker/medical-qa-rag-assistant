# 🏥 Medical QA Assistant - RAG System

> Production-ready medical question-answering system using Retrieval-Augmented Generation (RAG) on verified NIH medical sources.

## 🎯 Project Overview

AI-powered medical assistant providing accurate, source-cited answers using:
- **1,500+ verified Q&A pairs** from NIH sources (MedQuAD)
- **RAG architecture** to prevent LLM hallucinations
- **Citation system** for every answer

## 🚀 Live Demo

Try it here: [Hugging Face Space](https://huggingface.co/spaces/Lamloom/medical-qa-assistant)

## 🛠️ Tech Stack

- **Language**: Python 3.10+
- **RAG Framework**: LangChain concepts
- **Vector Database**: ChromaDB
- **Embeddings**: Sentence-Transformers (all-MiniLM-L6-v2)
- **LLM**: Google Gemini 2.5 Flash
- **UI**: Streamlit
- **Deployment**: Hugging Face Spaces

## 📊 Dataset

**MedQuAD** - Medical Question Answering Dataset
- Source: National Institutes of Health (NIH)
- 47,457 Q&A pairs from 12 medical sources

## 💡 Key Features

- ✅ Semantic search across medical knowledge base
- ✅ Source citation for every answer
- ✅ Hallucination prevention (only answers from verified sources)
- ✅ Recognizes when it lacks sufficient information
- ✅ Medical disclaimer on all responses

## 🔧 How It Works

1. User asks a medical question
2. System searches ChromaDB for relevant Q&A pairs
3. Top matches are sent to Gemini as context
4. Gemini generates a unified, cited answer

## 📂 Project Structure

- `medical_rag_system.py` - Core RAG system
- `01_data_exploration.ipynb` - Data processing & EDA
- `02_vector_database.ipynb` - Embeddings & ChromaDB
- `DATA_SETUP.md` - Dataset setup guide

## 👤 Author

**Lama Turki**
- GitHub: [@lamloom-maker](https://github.com/lamloom-maker)

## 📜 License

MIT License
