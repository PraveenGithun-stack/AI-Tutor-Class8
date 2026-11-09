# CURRICULUM BASED AI-TUTOR FOR CLASS 8 SCIENCE

# Project Overview
This project is an AI-powered educational tutor designed to answer Class 8 Science questions based on a predefined curriculum dataset.

# Objective
To build a syllabus-focused tutoring assistant that provides relevant answers only from the Class 8 Science textbook knowledge base.

# Dataset Used
- Custom dataset stored in JSONL format
- Contains syllabus-based science concepts and explanations

# Technologies Used
- Python
- Streamlit
- FAISS
- Sentence Transformers
- NumPy

# Methodology
1. Loaded textbook snippets from JSONL dataset
2. Generated embeddings using SentenceTransformer
3. Stored embeddings in FAISS vector database
4. Retrieved top relevant snippets for user query
5. Displayed answer and s…
[9:56 pm, 03/05/2026] Praveen: # Curriculum-Based AI Tutor for Class 8 Science

# Project Overview
This project is an AI-powered educational tutor designed to answer Class 8 Science questions based on a predefined curriculum dataset.

# Objective
To build a syllabus-focused tutoring assistant that provides relevant answers only from the Class 8 Science textbook knowledge base.

# Dataset Used
- Custom dataset stored in JSONL format
- Contains syllabus-based science concepts and explanations

# Technologies Used
- Python
- Streamlit
- FAISS
- Sentence Transformers
- NumPy

# Methodology
1. Loaded textbook snippets from JSONL dataset
2. Generated embeddings using SentenceTransformer
3. Stored embeddings in FAISS vector database
4. Retrieved top relevant snippets for user query
5. Displayed answer and source snippets in Streamlit UI

# Evaluation
The system was tested on multiple Class 8 Science questions.

| Metric | Value |
|--------|-------|
| Average Similarity Score | 0.94 |
| Accuracy (Relevant Answers) | 93% |

# Results
- Successfully answered syllabus-based questions
- Rejected out-of-syllabus/general knowledge questions

# Future Improvements
- Expand dataset for all science chapters
- Add voice input/output
- Deploy online for public access

# Conclusion
The project demonstrates a functional curriculum-aware AI tutor using retrieval-based semantic search and Streamlit deployment.