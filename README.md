# Movie Recommender System

A content-based movie recommendation system built using Python, Pandas, and Scikit-Learn.

## Project Status

✅ Data Collection  
✅ Data Cleaning  
✅ Feature Engineering  
⬜ Text Vectorization  
⬜ Cosine Similarity  
⬜ Recommendation Function  
⬜ Web App Deployment

---

## Dataset

Dataset used: TMDB 5000 Movie Dataset

Source:
https://www.kaggle.com/datasets/tmdb/tmdb-movie-metadata

Files used:
- tmdb_5000_movies.csv
- tmdb_5000_credits.csv

---

## Objective

The goal of this project is to recommend movies similar to a movie selected by the user using content-based filtering techniques.

---

## Technologies Used

- Python
- Pandas
- NumPy
- AST
- Jupyter Notebook

---

## Data Cleaning Steps Completed

### 1. Imported Datasets

Loaded:
- Movies dataset
- Credits dataset

### 2. Merged Datasets

Merged datasets using the movie title column.

### 3. Selected Relevant Features

Used the following columns:

- movie_id
- title
- overview
- genres
- keywords
- cast
- crew

### 4. Removed Missing Values

Removed rows containing null values using:

```python
movies.dropna(inplace=True)
```

### 5. Converted JSON-like Strings

Used `ast.literal_eval()` to convert string representations of lists into Python objects.

Example:

Before:

```text
'[{"id":28,"name":"Action"}]'
```

After:

```python
['Action']
```

### 6. Extracted Important Information

Extracted:

- Genre names
- Keyword names
- Top 3 cast members
- Director name from crew data

### 7. Removed Spaces

Converted names such as:

```text
Sam Worthington
```

to

```text
SamWorthington
```

to ensure they are treated as a single token.

### 8. Created Tags Column

Combined:

- Overview
- Genres
- Keywords
- Cast
- Crew

into a single feature column called `tags`.

### 9. Converted Tags into Text

Converted lists into a single text string using:

```python
" ".join(x)
```

Example:

Before:

```python
['Action', 'Adventure', 'Fantasy']
```

After:

```text
Action Adventure Fantasy
```

---

## Current Output

The dataset now contains:

| movie_id | title | tags |
|-----------|---------|---------|
| 19995 | Avatar | Action Adventure Fantasy ... |

This processed dataset will be used for:

- Text Vectorization
- Similarity Calculation
- Movie Recommendation Generation

---

## Next Steps

- Apply Stemming
- Convert Text into Vectors using CountVectorizer
- Calculate Cosine Similarity
- Build Recommendation Function
- Deploy Application

---

## Author

Nikki
