Project Name: Curriculum-Based AI Tutor

Description:
This project is an AI-powered tutor designed for NCERT Class 8 Science.
It uses Retrieval-Augmented Generation (RAG) with SentenceTransformer embeddings and FAISS vector search to answer only syllabus-based questions.

Technologies Used:
- Python
- Streamlit
- Sentence Transformers
- FAISS
- NumPy

Project Files:
- ai_tutor_class8.ipynb : Main notebook implementation
- class8_science.jsonl : Textbook knowledge base
- app.py : Streamlit web application
- README.txt : Project documentation

How to Run:
1. Install dependencies:
   pip install streamlit faiss-cpu sentence-transformers numpy

2. Run Streamlit App:
   python -m streamlit run app.py

Features:
- Textbook-based answer retrieval
- Semantic search using embeddings
- FAISS vector indexing
- Out-of-syllabus fallback response
- Source snippet transparency