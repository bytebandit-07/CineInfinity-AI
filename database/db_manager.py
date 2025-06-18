import mysql.connector
from database.db_config import get_connection
import os

conn = get_connection()
cursor = conn.cursor()

# Add a new user
def register_user(username, password, preferred_genres):
    try:
        # Check if user already exists
        cursor.execute("SELECT * FROM users WHERE username = %s", (username,))
        result = cursor.fetchone()
        if result:
            return "existed"

        # Join the list of genres into a string
        genre_string = ",".join(preferred_genres)

        # Insert new user with preferred genres
        cursor.execute(
            "INSERT INTO users (username, password, preferred_genres) VALUES (%s, %s, %s)",
            (username, password, genre_string)
        )
        conn.commit()
        return True

    except mysql.connector.Error:
        return False



def auth_user(username, password):
    try:
        cursor.execute("SELECT * FROM users WHERE username = %s AND password = %s", (username, password))
        result = cursor.fetchone()
        if result:
            print("✅ Authentication successful.")
            return result  # Return the full row so you can access user_id, etc.
        else:
            print("❌ Authentication failed. Invalid username or password.")
            return None
    except mysql.connector.Error as err:
        print(f"❌ Error during authentication: {err}")
        return None

# Log a search query for a user
def log_search(user_id, query):
    try:
        cursor.execute("INSERT INTO search_history (user_id, search_query) VALUES (%s, %s)", (user_id, query))
        conn.commit()
        print("✅ Search logged.")
    except mysql.connector.Error as err:
        print(f"❌ Error logging search: {err}")

# Retrieve search history for a user
def get_history(user_id):
    try:
        cursor.execute("SELECT search_query FROM search_history WHERE user_id = %s ORDER BY search_time DESC", (user_id,))
        return cursor.fetchall()
    except mysql.connector.Error as err:
        print(f"❌ Error retrieving history: {err}")
        return []

# Optional: Get user_id by username (for backend use)
def get_user_id(username):
    cursor.execute("SELECT id FROM users WHERE username = %s", (username,))
    result = cursor.fetchone()
    return result[0] if result else None

# Close the connection safely
def close():
    cursor.close()
    conn.close()

# not running
def preferred_movies(user_id):
    try:
        conn = get_connection()
        cursor = conn.cursor(dictionary=True)

        # Step 1: Fetch preferred genres from users table
        cursor.execute("SELECT preferred_genres FROM users WHERE user_id = %s", (user_id,))
        row = cursor.fetchone()

        if not row or not row["preferred_genres"]:
            print("❌ No preferred genres found for user.")
            return []

        genres_list = row["preferred_genres"].split()  # space-separated genres
        movies = []

        # Step 2: For each genre, get top-rated movies
        for genre in genres_list:
            query = """
                SELECT title, avg_rating AS rating, genres AS genre
                FROM movies
                WHERE genres LIKE %s
                ORDER BY avg_rating DESC
                LIMIT 10
            """
            cursor.execute(query, (f"%{genre}%",))
            results = cursor.fetchall()
            movies.extend(results)

        return movies

    except Exception as e:
        print(f"❌ Database error: {e}")
        return []

    finally:
        if conn.is_connected():
            cursor.close()
            conn.close()

def get_movies_by_genre(genre: str) -> list[dict[str, str]]:
    data = (f'%{genre}%',)
    result = []
    try:
        cursor.execute("SELECT movieid, title, genres, avg_rating FROM movies WHERE genres LIKE %s", data)
        rows = cursor.fetchall()
        for row in rows:
            movie_dict = {
                "movieId": str(row[0]),
                "title": row[1],
                "genres": row[2],
                "rating": str(row[3]),
                "description": "",
                'image': "placeholder.jpg" # Image path
            }
            result.append(movie_dict)
    except mysql.connector.Error as err:
        print(f"❌ Error retrieving history: {err}")
    return result

reult = preferred_movies(7)
print(reult)