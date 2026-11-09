AI Tutor – Class 8 Science

An AI-powered, curriculum-based learning assistant designed to help Class 8 students understand Science concepts through intelligent question answering and semantic search.

Project Overview

This project implements a Retrieval-Augmented Generation (RAG)-based AI tutoring system using textbook-based knowledge retrieval. It uses sentence embeddings and FAISS vector search to retrieve relevant educational content and provide context-aware answers.

Technologies Used

- Python
- Streamlit
- Sentence Transformers
- FAISS
- NumPy
- Semantic Search
- Retrieval-Augmented Generation (RAG)

Key Features

- Textbook-based question answering
- Semantic search using sentence embeddings
- FAISS-based vector indexing and retrieval
- Curriculum-oriented knowledge base
- Interactive Streamlit interface
- Out-of-syllabus fallback responses

Project Structure

AI-Tutor-Class8/
│
├── app.py
├── ai_tutor_class8.ipynb
├── class8_science.jsonl
├── evaluation.csv
├── log.txt
├── requirement.txt
├── README.md
├── report.md
└── .gitignore

Installation and Setup

1. Clone the repository

git clone https://github.com/PraveenGithun-stack/AI-Tutor-Class8.git

2. Navigate to the project directory

cd AI-Tutor-Class8

3. Install dependencies

pip install -r requirement.txt

4. Run the application

python -m streamlit run app.py

How It Works

1. Student enters a Science-related question.
2. Sentence Transformer converts the question into an embedding.
3. FAISS searches for relevant textbook content.
4. The application retrieves matching information.
5. The Streamlit interface displays the response.

Evaluation

The project includes an evaluation dataset ("evaluation.csv") and application logs for testing and analysis.

Detailed evaluation results can be added here after reporting the actual performance metrics.

Future Improvements

- Improve retrieval accuracy.
- Add more educational subjects.
- Integrate advanced language models.
- Deploy the application to a cloud platform.
- Improve the student learning experience.

Author

Praveen Githun

GitHub: https://github.com/PraveenGithun-stack

---

An AI-powered educational project combining machine learning, semantic search, and interactive application development.
