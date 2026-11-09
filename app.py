import streamlit as st
import json
import faiss
import numpy as np
from sentence_transformers import SentenceTransformer


chunks = []

with open("class8_science.jsonl", "r", encoding="utf-8") as f:
    for line in f:
        chunks.append(json.loads(line)["text"])


embed_model = SentenceTransformer("all-MiniLM-L6-v2")


embeddings = embed_model.encode(chunks)


embeddings = np.array(embeddings).astype("float32")

index = faiss.IndexFlatL2(embeddings.shape[1])
index.add(embeddings)


def search(query, k=3):
    query_embedding = embed_model.encode([query]).astype("float32")
    distances, indices = index.search(query_embedding, k)

    results = [chunks[i] for i in indices[0]]
    return results, distances[0]


def generate_answer(query):
    results, distances = search(query)

    if distances[0] > 1.0:
        return (
            "I'm focused on Class 8 Science. Please ask syllabus-based questions.",
            []
        )

    answer = results[0]
    return answer, results


st.title("Curriculum-Based AI Tutor")

query = st.text_input("Ask a Class 8 Science Question:")

if st.button("Get Answer"):
    if query:
        answer, sources = generate_answer(query)

        st.subheader("Answer")
        st.write(answer)

        st.subheader("Source Snippets")
        for s in sources:
            st.write("-", s)