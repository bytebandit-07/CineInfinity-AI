import pandas as pd
import mysql.connector
from dotenv import load_dotenv
import os

# Load environment variables from .env file
load_dotenv()

DB_HOST = os.getenv("DB_HOST")
DB_USER = os.getenv("DB_USER")
DB_PASSWORD = os.getenv("DB_PASSWORD")
DB_NAME = os.getenv("DB_NAME")

conn = mysql.connector.connect(
    host=DB_HOST,
    user=DB_USER,
    password=DB_PASSWORD,
    database=DB_NAME
)
cursor = conn.cursor()

# ✅ Load the CSV from your Downloads folder
df = pd.read_csv(r"C:\Users\omina\Downloads\processed_movies.csv").dropna()

# Insert each row into the movies table
for _, row in df.iterrows():
    try:
        cursor.execute(
            "INSERT INTO movies (movieId, title, genres, avg_rating) VALUES (%s, %s, %s, %s)",
            (int(row['movieId']), row['title'], row['genres'], float(row['avg_rating']))
        )
    except Exception as e:
        print(f"Error inserting row {row['movieId']}: {e}")

conn.commit()
cursor.close()
conn.close()

print("✅ Movies loaded successfully into the database.")
