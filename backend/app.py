# File: backend/app.py

from database.db_manager import register_user, auth_user, log_search, get_history
from model.recommender import recommend_by_title, recommend_by_user_history
from gemini_api.extract_movie_description import get_movie_description as fetch_description_from_api
from gui.image_scraper import get_image_url as fetch_image_from_scraper


class CineInfinityBackend:
    def __init__(self):
        self.user_id = None
        self.username = None

    def register(self, username: str, password: str, preferred_genres: list) -> str:
        return register_user(username, password, preferred_genres)

    def login(self, username: str, password: str) -> bool:
        user_data = auth_user(username, password)
        if user_data:
            self.user_id, self.username, _ = user_data
            print(f"Logged in as User ID: {self.user_id}, Username: {self.username}")
            return True
        return False

    def recommend(self, movie_title: str, n_recommendations: int = 10) -> list[dict]:
        """
        Gets base movie recommendations. No longer fetches descriptions/images here.
        """
        if self.user_id:
            log_search(self.user_id, movie_title)

        # Returns a list of dicts with: title, genres, avg_rating, etc.
        return recommend_by_title(movie_title, n_recommendations)

    def get_movie_description(self, movie_title: str) -> str:
        """Wrapper method to fetch a single movie description."""
        return fetch_description_from_api(movie_title)

    def get_image_url(self, movie_title: str) -> str:
        """Wrapper method to fetch a single image url."""
        return fetch_image_from_scraper(movie_title)

    def get_user_history(self) -> list[str]:
        if self.user_id:
            return get_history(self.user_id)
        return []

    def close_db_connection(self):
        from database.db_manager import close as close_db
        close_db()
        print("Database connection closed.")