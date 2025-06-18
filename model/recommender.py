import pandas as pd
import pickle

from sklearn.metrics.pairwise import cosine_similarity
from sklearn.neighbors import NearestNeighbors

# Paths to models and dataset
TFIDF_MODEL_PATH = "../model/tfidf_vectorizer.pkl"
KNN_MODEL_PATH = "../model/knn_movie_model.pkl"
PROCESSED_DATA_PATH = "../notebook/processed_movies.csv"


# Load models and data once
def load_models_and_data():
    with open(TFIDF_MODEL_PATH, "rb") as f:
        tfidf = pickle.load(f)
    with open(KNN_MODEL_PATH, "rb") as f:
        knn = pickle.load(f)
    movies = pd.read_csv(PROCESSED_DATA_PATH)
    return tfidf, knn, movies


# Recommend movies based on title
def recommend_by_title(movie_title: str, n_recommendations: int = 5):
    tfidf, knn, movies = load_models_and_data()

    # Try to find the movie
    matches = movies[movies['title'].str.contains(movie_title, case=False)]
    if matches.empty:
        print(f"❌ No movie found with title: {movie_title}")
        return []

    # Use first matching result
    idx = matches.index[0]
    input_movie = movies.iloc[idx]

    input_vector = tfidf.transform([input_movie['genres']])
    distances, indices = knn.kneighbors(input_vector, n_neighbors=n_recommendations + 1)

    recommendations = []
    for i, dist in zip(indices[0][1:], distances[0][1:]):
        movie = movies.iloc[i]
        recommendations.append({
            'movieId': movie['movieId'],
            'title': movie['title'],
            'genres': movie['genres'],
            'avg_rating': round(movie['avg_rating'], 1),
            'similarity': round(1 - dist, 3)
        })

    return recommendations


# 🧑 Recommend for a user based on search history
def recommend_by_user_history(user_history_titles: list, n_recommendations: int = 5):
    tfidf, knn, movies = load_models_and_data()

    genre_texts = []
    for title in user_history_titles:
        matches = movies[movies['title'].str.contains(title, case=False)]
        if not matches.empty:
            genre_texts.append(matches.iloc[0]['genres'])

    if not genre_texts:
        print("❌ No valid movies found in history.")
        return []

    # Aggregate genres from history
    combined_genres = " ".join(genre_texts)
    input_vector = tfidf.transform([combined_genres])
    distances, indices = knn.kneighbors(input_vector, n_neighbors=n_recommendations + 1)

    recommendations = []
    for i, dist in zip(indices[0], distances[0]):
        movie = movies.iloc[i]
        if movie['title'] not in user_history_titles:  # avoid suggesting same ones
            recommendations.append({
                'movieId': movie['movieId'],
                'title': movie['title'],
                'genres': movie['genres'],
                'rating': round(movie['avg_rating'], 1),
                'description': "" # To be filled later
            })

        if len(recommendations) >= n_recommendations:
            break

    return recommendations

