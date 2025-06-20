import mysql.connector
from database.db_config import get_connection

# It's generally better to manage connections within a class or pass them as arguments,
# but for this structure, we'll use a single global connection.
conn = get_connection()
cursor = conn.cursor()


def register_user(username, password, preferred_genres):
    """Adds a new user to the database."""
    try:
        # Check if user already exists
        cursor.execute("SELECT * FROM users WHERE username = %s", (username,))
        if cursor.fetchone():
            return "existed"

        # Join the list of genres into a comma-separated string
        genre_string = ",".join(preferred_genres)

        cursor.execute(
            "INSERT INTO users (username, password, preferred_genres) VALUES (%s, %s, %s)",
            (username, password, genre_string)
        )
        conn.commit()
        return True
    except mysql.connector.Error as err:
        print(f"❌ Error during registration: {err}")
        conn.rollback()  # Rollback changes on error
        return False


def auth_user(username, password):
    """Authenticates a user and returns their data if successful."""
    try:
        # Select specific columns instead of '*'
        cursor.execute("SELECT user_id, username, preferred_genres FROM users WHERE username = %s AND password = %s",
                       (username, password))
        result = cursor.fetchone()
        if result:
            print("✅ Authentication successful.")
            return result
        else:
            print("❌ Authentication failed. Invalid username or password.")
            return None
    except mysql.connector.Error as err:
        print(f"❌ Error during authentication: {err}")
        return None


def log_search(user_id, query):
    """Logs a search query for a specific user."""
    try:
        cursor.execute("INSERT INTO search_history (user_id, search_query) VALUES (%s, %s)", (user_id, query))
        conn.commit()
        print("✅ Search logged.")
    except mysql.connector.Error as err:
        print(f"❌ Error logging search: {err}")
        conn.rollback()


def get_history(user_id):
    """Retrieves search history for a user as a list of strings."""
    try:
        # REMOVE the 'ORDER BY' part from this query
        cursor.execute("SELECT search_query FROM search_history WHERE user_id = %s", (user_id,))
        return [row[0] for row in cursor.fetchall()]
    except mysql.connector.Error as err:
        print(f"❌ Error retrieving history: {err}")
        return []


def get_user_id(username):
    """Gets a user's ID from their username."""
    try:
        cursor.execute("SELECT user_id FROM users WHERE username = %s", (username,))
        result = cursor.fetchone()
        return result[0] if result else None
    except mysql.connector.Error as err:
        print(f"❌ Error getting user ID: {err}")
        return None


def get_movies_by_genre(genre, limit=20):
    """Retrieves a list of movies for a given genre."""
    dict_cursor = None
    try:
        # Using a dictionary cursor makes handling results easier
        dict_cursor = conn.cursor(dictionary=True)
        query = "SELECT title, genres, avg_rating FROM movies WHERE genres LIKE %s ORDER BY avg_rating DESC LIMIT %s"
        dict_cursor.execute(query, (f"%{genre}%", limit))
        return dict_cursor.fetchall()
    except mysql.connector.Error as err:
        print(f"❌ Error retrieving movies by genre: {err}")
        return []
    finally:
        if dict_cursor:
            dict_cursor.close()


def get_preferred_movies(user_id):
    """Gets movie recommendations based on a user's preferred genres."""
    dict_cursor = None
    try:
        dict_cursor = conn.cursor(dictionary=True)
        # Step 1: Get user's preferred genres
        dict_cursor.execute("SELECT preferred_genres FROM users WHERE user_id = %s", (user_id,))
        user_prefs = dict_cursor.fetchone()

        if not user_prefs or not user_prefs["preferred_genres"]:
            print("❌ No preferred genres found for this user.")
            return []

        # CORRECTED: Split by comma, not space
        genres_list = user_prefs["preferred_genres"].split(',')
        movies = []

        # Step 2: Fetch top movies for each genre
        for genre in genres_list:
            if not genre: continue  # Skip empty strings
            # Reuse the get_movies_by_genre function to avoid duplicate code
            movies.extend(get_movies_by_genre(genre.strip(), limit=5))  # Get 5 movies per genre

        # Remove duplicate movies that might appear in multiple genres
        unique_movies = {movie['title']: movie for movie in movies}.values()
        return list(unique_movies)

    except mysql.connector.Error as err:
        print(f"❌ Database error in get_preferred_movies: {err}")
        return []
    finally:
        if dict_cursor:
            dict_cursor.close()


def close():
    """Safely closes the database connection and cursor."""
    if cursor:
        cursor.close()
    if conn and conn.is_connected():
        conn.close()
        print("Database connection closed.")