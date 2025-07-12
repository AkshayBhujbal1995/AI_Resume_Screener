
# 🤖 AI Resume Screener with NLP and Machine Learning

This project is an **AI-powered resume screening tool** built using Python. It reads resumes in **PDF format**, extracts their text using **PyMuPDF**, preprocesses them with **Natural Language Processing (NLP)**, and calculates **match scores** against a job description using **TF-IDF and cosine similarity**.

---

## 📌 Project Highlights

- 📄 Reads multiple resumes from a folder
- 🔍 Extracts and cleans text using NLP
- 🧠 Compares resumes to a job description
- 📈 Ranks candidates based on relevance score

---

## 🧪 Technologies Used

| Tool | Purpose |
|------|---------|
| `PyMuPDF` | PDF text extraction |
| `nltk` | Stopwords removal |
| `scikit-learn` | TF-IDF vectorization & cosine similarity |
| `pandas` / `numpy` | Data handling |

---

## 🧠 How It Works

### ✅ Step 1: Extract Text from Resume PDFs

```python
import fitz  # PyMuPDF

def extract_text_from_pdf(pdf_path):
    text = ""
    with fitz.open(pdf_path) as doc:
        for page in doc:
            text += page.get_text("text") + "\n"
    return text
````

---

### ✅ Step 2: Preprocess Text (NLP)

```python
import re
from nltk.corpus import stopwords

def preprocess_text(text):
    text = text.lower()
    text = re.sub(r'[^\w\s]', '', text)
    text = ' '.join([word for word in text.split() if word not in stopwords.words('english')])
    return text
```

* ✅ Converts to lowercase
* ✅ Removes punctuation
* ✅ Removes common English stopwords

---

### ✅ Step 3: Compute Match Score Using TF-IDF + Cosine Similarity

```python
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

vectorizer = TfidfVectorizer()
vectors = vectorizer.fit_transform([clean_job_description, clean_resume_text])
similarity_score = cosine_similarity(vectors)[0][1]
```

* 💡 Output: A similarity score between `0` and `1`
* Example: `Resume Match Score: 0.31`

---

### ✅ Step 4: Rank All Resumes in Folder

```python
resume_scores = {}
for resume_file in os.listdir(resume_folder):
    resume_text = extract_text_from_pdf(os.path.join(resume_folder, resume_file))
    clean_resume_text = preprocess_text(resume_text)
    vectors = vectorizer.transform([clean_job_description, clean_resume_text])
    similarity_score = cosine_similarity(vectors)[0][1]
    resume_scores[resume_file] = similarity_score

sorted_resumes = sorted(resume_scores.items(), key=lambda x: x[1], reverse=True)
```

* 📄 Each resume is assigned a similarity score
* 📊 Output (Ranked Results):

```
Akshay-Bhujbal_Data-Analyst_CV.pdf: 0.27
Akshay_Bhujbal_DA_CV.pdf: 0.26
AkshayBhujbalResume.pdf: 0.25
```

---

## 📦 Installation & Dependencies

```bash
pip install pandas numpy PyMuPDF nltk scikit-learn
```

Also download stopwords if not already done:

```python
import nltk
nltk.download('stopwords')
```

---

## 📁 Folder Structure

```
AI_Resume_Screener.ipynb
README.md
app.py
```

---

## 🚀 How to Use

1. 🔁 Add all resumes (PDFs) to the `resumes/` folder
2. ✍️ Edit the job description string in the code
3. ▶️ Run the notebook
4. 📊 See ranked results printed at the end

---

## 📌 Use Cases

* HR / Recruiters for automated resume screening
* Job seekers comparing their resume with job descriptions
* Developers experimenting with NLP + similarity scoring

---

## 👨‍💻 About the Author

**Akshay Bhujbal**

* 📍 Pune, India
* 📊 Data Analyst | Resume Screening AI Enthusiast
* 🔗 [GitHub](https://github.com/AkshayBhujbal1995)
* 💼 [LinkedIn](https://linkedin.com/in/akshay-1995-bhujbal)

---

## ⭐ If You Like This Project

Please ⭐ star the repository and share it with others!

---

