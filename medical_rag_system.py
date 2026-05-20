
"""
Medical QA RAG System
=====================
A Retrieval-Augmented Generation system for medical Q&A
using ChromaDB + Sentence Transformers + Gemini LLM.

Author: Lama Turki
Date: May 2026
"""

import pandas as pd
import numpy as np
from sentence_transformers import SentenceTransformer
import chromadb
import google.generativeai as genai


class MedicalRAGSystem:
    """Medical Question-Answering RAG System"""
    
    def __init__(self, gemini_api_key, chroma_path="./chroma_db"):
        """Initialize the RAG system"""
        # Load embedding model
        self.embedding_model = SentenceTransformer("all-MiniLM-L6-v2")
        
        # Connect to ChromaDB
        self.chroma_client = chromadb.PersistentClient(path=chroma_path)
        self.collection = self.chroma_client.get_collection("medical_qa")
        
        # Setup Gemini
        genai.configure(api_key=gemini_api_key)
        self.llm = genai.GenerativeModel("gemini-2.5-flash")
        
        print("Medical RAG System initialized successfully!")
    
    def search(self, query, top_k=3):
        """Search for relevant documents"""
        query_embedding = self.embedding_model.encode([query]).tolist()
        results = self.collection.query(
            query_embeddings=query_embedding,
            n_results=top_k
        )
        
        formatted_results = []
        for i in range(len(results["ids"][0])):
            formatted_results.append({
                "similarity": 1 - results["distances"][0][i],
                "question": results["metadatas"][0][i]["question"],
                "answer": results["documents"][0][i],
                "source": results["metadatas"][0][i]["source"]
            })
        return formatted_results
    
    def ask(self, query, top_k=3):
        """Complete RAG pipeline: search + generate"""
        # Search
        results = self.search(query, top_k=top_k)
        
        # Build context
        context = "\n\n".join([
            f"--- Source {i+1}: {r['source']} ---\n"
            f"Q: {r['question']}\nA: {r['answer']}"
            for i, r in enumerate(results)
        ])
        
        # Build prompt
        prompt = f"""You are a helpful medical assistant. Answer based ONLY on 
the verified sources below. Cite sources and add a medical disclaimer.

SOURCES:
{context}

QUESTION: {query}

ANSWER:"""
        
        # Generate response
        response = self.llm.generate_content(prompt)
        
        return {
            "answer": response.text,
            "sources": results,
            "query": query
        }


if __name__ == "__main__":
    # Example usage
    rag = MedicalRAGSystem(gemini_api_key="YOUR_KEY_HERE")
    result = rag.ask("What are the symptoms of diabetes?")
    print(result["answer"])
