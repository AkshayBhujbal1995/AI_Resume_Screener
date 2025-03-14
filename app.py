import streamlit as st
import PyPDF2
import numpy as np
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

# Function to extract text from PDFs
def extract_text_from_pdf(uploaded_file):
    text = ""
    reader = PyPDF2.PdfReader(uploaded_file)
    for page in reader.pages:
        text += page.extract_text() if page.extract_text() else ""
    return text

# Function to preprocess text (basic cleanup)
def preprocess_text(text):
    return text.lower().strip()

# Streamlit UI
st.title("Akshay Bhujbal's AI Resume Screener")
st.subheader("Upload Resumes & Get AI Rankings")

st.write(
    "Most resume checkers allow only a few uploads per day or charge fees. "
    "This tool is completely free and unlimited. Upload your resumes and see the rankings instantly."
)

# Upload resumes
uploaded_files = st.file_uploader("Upload resumes (PDF only)", accept_multiple_files=True, type=["pdf"])
job_desc = st.text_area("Paste the Job Description here")

if st.button("Rank Resumes"):
    if not uploaded_files:
        st.warning("Please upload at least one resume.")
    elif not job_desc.strip():
        st.warning("Please enter a job description.")
    else:
        resume_scores = {}

        # Initialize TF-IDF Vectorizer
        vectorizer = TfidfVectorizer()

        # Process resumes
        for uploaded_file in uploaded_files:
            resume_text = extract_text_from_pdf(uploaded_file)
            clean_resume_text = preprocess_text(resume_text)

            # Fit vectorizer on job description and resume
            documents = [job_desc, clean_resume_text]
            vectors = vectorizer.fit_transform(documents)

            # Compute similarity
            similarity_score = cosine_similarity(vectors)[0][1]
            resume_scores[uploaded_file.name] = similarity_score

        # Sort resumes by match score
        sorted_resumes = sorted(resume_scores.items(), key=lambda x: x[1], reverse=True)

        # Display results
        st.subheader("Ranked Resumes")
        for resume, score in sorted_resumes:
            st.write(f"{resume}: {score:.2%} match")

        st.success("Ranking Complete!")
