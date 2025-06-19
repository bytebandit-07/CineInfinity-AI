import pandas as pd
import pickle

from pycparser.ply.yacc import resultlimit
from sklearn.metrics.pairwise import cosine_similarity
from sklearn.neighbors import NearestNeighbors

# Paths to models and dataset (absolute way, sochange according to yours)
TFIDF_MODEL_PATH = "C:\\Users\\talha\\Documents\\Semester 4\\Artificial Intelligence\\Project\\CineInfinity-Ai\\model\\tfidf_vectorizer.pkl"
KNN_MODEL_PATH = "C:\\Users\\talha\\Documents\\Semester 4\\Artificial Intelligence\\Project\\CineInfinity-Ai\\model\\knn_movie_model.pkl"
PROCESSED_DATA_PATH = "C:\\Users\\talha\\Documents\\Semester 4\\Artificial Intelligence\\Project\\CineInfinity-Ai\\notebook\\processed_movies.csv"


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

    matches = movies[movies['title'].str.contains(movie_title, case=False)]
    if matches.empty:
        print(f"No movie found with title: {movie_title}")
        return []

    idx = matches.index[0]
    input_movie = movies.iloc[idx]

    input_vector = tfidf.transform([input_movie['genres']])
    distances, indices = knn.kneighbors(input_vector, n_neighbors=n_recommendations + 1)

    recommendations = []
    for i, dist in zip(indices[0][1:], distances[0][1:]):
        movie = movies.iloc[i]
        recommendations.append({
            'movieId': int(movie['movieId']),
            'title': movie['title'],
            'genres': movie['genres'],
            'avg_rating': round(float(movie['avg_rating']), 1),
            'similarity': round((1 - float(dist)) * 100, 2)
        })

    return recommendations


# Recommend for a user based on search history
def recommend_by_user_history(user_history_titles: list, n: int = 10):
    tfidf, knn, movies = load_models_and_data()
    genres = []

    history_lower = [t.lower() for t in user_history_titles]
    for title in history_lower:
        match = movies[movies['title'].str.lower().str.contains(title)]
        if not match.empty:
            genres.append(match.iloc[0]['genres'])

    if not genres:
        return []

    input_vec = tfidf.transform([" ".join(genres)])
    distances, indices = knn.kneighbors(input_vec, n_neighbors=n + 10)

    recs = []
    for i, dist in zip(indices[0], distances[0]):
        movie = movies.iloc[i]
        if all(h not in movie['title'].lower() for h in history_lower):
            recs.append({
                'movieId': movie['movieId'],
                'title': movie['title'],
                'genres': movie['genres'],
                'rating': round(movie['avg_rating'], 1),
                'similarity': round((1 - float(dist)) * 100, 2)
            })
        if len(recs) == n:
            break

    return recs

# just testing for functions
# title one
result = recommend_by_title("Interstellar")
print(result)


# list one
history = ["Interstellar", "Inception", "Watchmen"]
recs = recommend_by_user_history(history)

for rec in recs:
    print(f"{rec['movieId']} - {rec['title']} - {rec['genres']} - {rec['rating']} - Similarity: {rec['similarity']}")
