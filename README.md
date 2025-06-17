# 🎬 Movie Recommendation System

A **content-based movie recommendation system** built using **Streamlit**. It suggests movies similar to a user-selected title by analyzing content features such as plot keywords, genres, and cast.

---

## 🚀 Features

- 🎥 **Movie Recommendations**: Suggests the top 5 similar movies.
- 🧠 **Content-Based Filtering**: Uses metadata features like cast, genres, and keywords.
- 🖼️ **Poster Integration**: Fetches movie posters dynamically from the [OMDb API](http://www.omdbapi.com/).
- 📊 **Similarity Visualization**: Displays similarity scores with progress bars.
- 💡 **User-Friendly Interface**: Built with Streamlit for clean, interactive UI.

---

## ⚙️ Technical Overview

This system uses **content-based filtering** and **cosine similarity** to recommend similar movies.

### ✅ Step-by-Step Breakdown:

1. **🛠️ Data Preparation**:
   - Movie metadata like title, genres, cast, and keywords are combined into a "metadata soup".
   - Example: `"Action Tom Hanks Adventure Space"`

2. **🔢 Feature Extraction**:
   - The metadata soup is vectorized using **CountVectorizer** from `scikit-learn`.
   - A feature matrix is generated where each row represents a movie.

3. **📐 Similarity Computation**:
   - **Cosine Similarity** is calculated between movie vectors.
   - This forms a similarity matrix (`similarity.pkl`) that quantifies how close each pair of movies is.

4. **🎯 Recommendation Engine**:
   - On movie selection, the top 5 most similar movies (excluding the selected one) are retrieved and sorted by similarity score.

5. **🖼️ Poster Fetching**:
   - Poster URLs are fetched from **OMDb API** using the movie title and year.

6. **🌐 UI Presentation**:
   - The UI is built in **Streamlit**, displaying recommendations with posters and similarity bars.

---

## 🛠️ Tech Stack

- `Python`
- `Streamlit`
- `Pandas`
- `scikit-learn`
- `Pickle`
- `OMDb API`

---

## 📦 Setup Instructions

```bash
# 1. Clone the repository
git clone https://github.com/your-username/movie-recommender.git
cd movie-recommender

# 2. Install dependencies
pip install -r requirements.txt

# 3. (Optional) Add your OMDb API key in the script

# 4. Run the Streamlit app
streamlit run app.py
