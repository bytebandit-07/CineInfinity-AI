# db_manager.py

import mysql.connector
from dotenv import load_dotenv
import os

# Load environment variables from .env file
load_dotenv()

DB_HOST = os.getenv("DB_HOST")
DB_USER = os.getenv("DB_USER")
DB_PASSWORD = os.getenv("DB_PASSWORD")
DB_NAME = os.getenv("DB_NAME")

# Establish connection
conn = mysql.connector.connect(
    host=DB_HOST,
    user=DB_USER,
    password=DB_PASSWORD,
    database=DB_NAME
)
cursor = conn.cursor()

# Add a new user
def add_user(username, password):
    try:
        cursor.execute("INSERT INTO users (username, password) VALUES (%s, %s)", (username, password))
        conn.commit()
        print("✅ User added successfully.")
    except mysql.connector.Error as err:
        print(f"❌ Error adding user: {err}")

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
        cursor.execute("SELECT search_query, search_time FROM search_history WHERE user_id = %s ORDER BY search_time DESC", (user_id,))
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
