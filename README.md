# 🎬 Movie Recommender System

A Content-Based Movie Recommendation System built using NLP techniques and Machine Learning. The system recommends movies similar to a selected movie by analyzing genres, cast, crew, keywords, and movie overviews.

---

## 🚀 Features

- Content-Based Filtering
- Natural Language Processing (NLP)
- Text Preprocessing and Stemming
- Bag of Words Vectorization
- Cosine Similarity-Based Recommendations
- Interactive Streamlit Web Application

---

## 📊 Dataset

TMDB 5000 Movie Dataset

Source:
https://www.kaggle.com/datasets/tmdb/tmdb-movie-metadata

Files used:

- tmdb_5000_movies.csv
- tmdb_5000_credits.csv

---

## 🛠️ Tech Stack

- Python
- Pandas
- NumPy
- Scikit-Learn
- NLTK
- Streamlit

---

## 📌 Project Workflow

### 1. Data Collection

Loaded movie metadata and credits datasets from TMDB.

### 2. Data Preprocessing

- Removed missing values
- Merged datasets
- Selected relevant features
- Extracted director information
- Extracted top cast members
- Processed genres and keywords

### 3. Feature Engineering

Created a combined `tags` feature using:

- Overview
- Genres
- Keywords
- Cast
- Crew

### 4. Text Processing

Applied:

- Lowercasing
- Tokenization
- Stemming using Porter Stemmer

### 5. Vectorization

Converted movie tags into numerical vectors using:

```python
CountVectorizer(max_features=5000, stop_words='english')
```

### 6. Similarity Calculation

Calculated movie similarity using:

```python
cosine_similarity()
```

### 7. Recommendation Generation

Generated Top-5 movie recommendations based on cosine similarity scores.

---

## 📈 Results

- Processed 4,800+ movies
- Generated 5,000-dimensional feature vectors
- Built a similarity matrix for movie recommendations
- Successfully deployed recommendation logic through a Streamlit interface

---

## 📂 Project Structure

```text
movie-recommender-system/
│
├── app.py
├── create_model.py
├── movie_dict.pkl
├── similarity.pkl
├── README.md
```

---

## ▶️ Running the Project

Install dependencies:

```bash
pip install pandas numpy scikit-learn nltk streamlit
```

Run the application:

```bash
streamlit run app.py
```

---

## 🎯 Sample Recommendation

Input:

```text
Batman Begins
```

Output:

```text
The Dark Knight
Batman
The Dark Knight Rises
10th & Wolf
```

---

## 👩‍💻 Author

Pratishtha Garg
