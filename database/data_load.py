import pandas as pd
from db_config import get_connection

# Get DB connection
conn = get_connection()
cursor = conn.cursor()

# ✅ Load the CSV
df = pd.read_csv(r"..\notebook\processed_movies.csv").dropna()

# Insert rows
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