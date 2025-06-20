import pandas as pd
import pickle
import os

# --- Path Setup & Model Loading (Optimized) ---

# This section runs only once when the module is imported.
try:
    # Use relative paths to make the code portable
    BASE_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
    TFIDF_MODEL_PATH = os.path.join(BASE_DIR, "model", "tfidf_vectorizer.pkl")
    KNN_MODEL_PATH = os.path.join(BASE_DIR, "model", "knn_movie_model.pkl")
    PROCESSED_DATA_PATH = os.path.join(BASE_DIR, "notebook", "processed_movies.csv")

    # Load all models and data into memory for fast access
    with open(TFIDF_MODEL_PATH, "rb") as f:
        _tfidf = pickle.load(f)
    with open(KNN_MODEL_PATH, "rb") as f:
        _knn = pickle.load(f)

    _movies = pd.read_csv(PROCESSED_DATA_PATH)
    print("✅ Recommender models and data loaded successfully.")

except FileNotFoundError as e:
    print(f"❌ CRITICAL ERROR: Could not load recommender models. {e}")
    # Set to None so the app knows the recommender is offline
    _tfidf, _knn, _movies = None, None, None


# --- Recommendation Functions ---

def recommend_by_title(movie_title: str, n_recommendations: int = 10) -> list:
    """Recommends movies based on the genre similarity to a given movie title."""
    if _tfidf is None:  # Check if models loaded correctly
        return []

    # Find the movie in the dataframe
    matches = _movies[_movies['title'].str.contains(movie_title, case=False)]
    if matches.empty:
        print(f"❌ No movie found matching title: {movie_title}")
        return []

    # Use the first match as input
    idx = matches.index[0]
    input_movie_genres = _movies.iloc[idx]['genres']

    # Get recommendations from the KNN model
    input_vector = _tfidf.transform([input_movie_genres])
    distances, indices = _knn.kneighbors(input_vector, n_neighbors=n_recommendations + 1)

    recommendations = []
    # Skip the first index [0] because it's the movie itself
    for i, dist in zip(indices[0][1:], distances[0][1:]):
        movie = _movies.iloc[i]
        recommendations.append({
            'movieId': int(movie['movieId']),
            'title': movie['title'],
            'genres': movie['genres'],
            'avg_rating': round(float(movie['avg_rating']), 1),
            'similarity': round((1 - float(dist)) * 100, 1)  # As a percentage
        })

    return recommendations


def recommend_by_user_history(user_history_titles: list, n_recommendations: int = 10) -> list:
    """Recommends movies based on a user's entire search history."""
    if _tfidf is None:  # Check if models loaded correctly
        return []

    # Aggregate genres from all movies in the user's history
    genre_texts = []
    history_lower = [title.lower() for title in user_history_titles]

    for title in history_lower:
        matches = _movies[_movies['title'].str.lower().str.contains(title)]
        if not matches.empty:
            genre_texts.append(matches.iloc[0]['genres'])

    if not genre_texts:
        print("❌ No valid movies found in user history to base recommendations on.")
        return []

    # Create a single "taste" vector from all historical genres
    combined_genres = " ".join(genre_texts)
    input_vector = _tfidf.transform([combined_genres])

    # Get more recommendations than needed to filter out already-seen movies
    distances, indices = _knn.kneighbors(input_vector, n_neighbors=n_recommendations + len(history_lower) + 5)

    recommendations = []
    for i, dist in zip(indices[0], distances[0]):
        movie = _movies.iloc[i]
        # Ensure we don't recommend a movie that's already in the history
        is_in_history = any(h in movie['title'].lower() for h in history_lower)

        if not is_in_history:
            recommendations.append({
                'movieId': int(movie['movieId']),
                'title': movie['title'],
                'genres': movie['genres'],
                'avg_rating': round(float(movie['avg_rating']), 1),
                'similarity': round((1 - float(dist)) * 100, 1)  # As a percentage
            })

        # Stop once we have enough recommendations
        if len(recommendations) >= n_recommendations:
            break

    return recommendations


# --- Standalone Testing ---
if __name__ == '__main__':
    print("\n--- Testing recommend_by_title ---")
    title_recs = recommend_by_title("Interstellar", n_recommendations=5)
    if title_recs:
        for rec in title_recs:
            print(f"  > {rec['title']} ({rec['genres']}) - Similarity: {rec['similarity']}%")

    print("\n--- Testing recommend_by_user_history ---")
    history = ["Interstellar", "Inception", "Watchmen", "The Dark Knight"]
    history_recs = recommend_by_user_history(history, n_recommendations=10)

    if history_recs:
        for rec in history_recs:
            print(f"  > {rec['title']} ({rec['genres']}) - Similarity: {rec['similarity']}%")