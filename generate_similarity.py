import pickle
import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

# Load movies dictionary
movies_dict = pickle.load(open('movies_dict.pkl', 'rb'))
movies = pd.DataFrame(movies_dict)

print("Columns in movies DataFrame:", movies.columns)
print("Sample data from movies DataFrame:")
print(movies.head())

# Use the 'tags' column directly for similarity
if 'tags' not in movies.columns:
    raise ValueError("The 'tags' column is missing from the movies data.")

print("Using 'tags' column for similarity vectorization.")
tfidf = TfidfVectorizer(stop_words='english')
tfidf_matrix = tfidf.fit_transform(movies['tags'])

# Compute cosine similarity matrix
similarity = cosine_similarity(tfidf_matrix)

# Save similarity matrix
with open('similarity.pkl', 'wb') as f:
    pickle.dump(similarity, f)

print("similarity.pkl file has been created successfully.")
