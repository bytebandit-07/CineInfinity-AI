import tkinter as tk
import customtkinter as ctk
from PIL import Image, ImageTk


def search_movie():
    movie = entry.get()
    print(f"Searching for recommendations based on: {movie}")
    # Add search functionality here


# Sample movie data
movie_categories = {
    "Trending Now": [
        {"title": "Movie 1", "image": "placeholder.jpg"},
        {"title": "Movie 2", "image": "placeholder.jpg"},
        {"title": "Movie 3", "image": "placeholder.jpg"},
        {"title": "Movie 4", "image": "placeholder.jpg"},
        {"title": "Movie 5", "image": "placeholder.jpg"},
    ],
    "Comedy Movies": [
        {"title": "Funny Movie 1", "image": "placeholder.jpg"},
        {"title": "Funny Movie 2", "image": "placeholder.jpg"},
        {"title": "Funny Movie 3", "image": "placeholder.jpg"},
        {"title": "Funny Movie 4", "image": "placeholder.jpg"},
        {"title": "Funny Movie 5", "image": "placeholder.jpg"},
    ],
    "Horror Movies": [
        {"title": "Scary Movie 1", "image": "placeholder.jpg"},
        {"title": "Scary Movie 2", "image": "placeholder.jpg"},
        {"title": "Scary Movie 3", "image": "placeholder.jpg"},
        {"title": "Scary Movie 4", "image": "placeholder.jpg"},
        {"title": "Scary Movie 5", "image": "placeholder.jpg"},
    ],
    "Suspense Thrillers": [
        {"title": "Thriller 1", "image": "placeholder.jpg"},
        {"title": "Thriller 2", "image": "placeholder.jpg"},
        {"title": "Thriller 3", "image": "placeholder.jpg"},
        {"title": "Thriller 4", "image": "placeholder.jpg"},
        {"title": "Thriller 5", "image": "placeholder.jpg"},
    ]
}

root = ctk.CTk()
ctk.set_appearance_mode("dark")
root.geometry("900x600")
root.title("Film Flow")

# --- Top Menu Frame ---
menu_frame = ctk.CTkFrame(root, fg_color="#E50914", corner_radius=0)
menu_frame.pack(fill="x", padx=0, pady=0)

menu_inner = ctk.CTkFrame(menu_frame, fg_color="#E50914")  # container for horizontal layout
menu_inner.pack(padx=10, pady=10, fill="x")

title_label = ctk.CTkLabel(menu_inner, text="Film Flow", text_color="white", font=("morganite", 22, "bold"))
title_label.pack(side="left", padx=(5, 20))

search_bar = ctk.CTkEntry(menu_inner, placeholder_text="Search", placeholder_text_color="black",
                          width=500, height=30, fg_color="#f0f0f0", text_color="black",
                          border_width=0, corner_radius=150, justify="center")
search_bar.pack(side="left", padx=(290, 10))
search_bar.bind("<Return>", lambda event: search_movie())
entry = search_bar

# --- Main Scrollable Content ---
content_frame = ctk.CTkScrollableFrame(root, fg_color="black")
content_frame.pack(fill="both", expand=True)

selected_movie_frame = None


def on_movie_select(frame, movie_data):
    global selected_movie_frame

    if selected_movie_frame:
        selected_movie_frame.configure(border_width=0, fg_color="#333333")

    frame.configure(border_width=2, border_color="#E50914", fg_color="#444444")
    selected_movie_frame = frame

    print(f"Selected movie: {movie_data['title']}")


# --- Populate Movie Sections ---
for category, movies in movie_categories.items():
    category_label = ctk.CTkLabel(content_frame, text=category, text_color="white",
                                  font=("Arial", 18, "bold"), anchor="w")
    category_label.pack(fill="x", padx=20, pady=(20, 10))

    movie_row = ctk.CTkFrame(content_frame, fg_color="black")
    movie_row.pack(fill="x", padx=20, pady=(0, 20))

    for movie in movies:
        poster_frame = ctk.CTkFrame(movie_row, width=150, height=220,
                                    fg_color="#333333", corner_radius=10)
        poster_frame.pack_propagate(False)
        poster_frame.pack(side="left", padx=10)

        def on_enter(e, frame=poster_frame):
            if frame != selected_movie_frame:
                frame.configure(fg_color="#3a3a3a")

        def on_leave(e, frame=poster_frame):
            if frame != selected_movie_frame:
                frame.configure(fg_color="#333333")

        poster_frame.bind("<Enter>", on_enter)
        poster_frame.bind("<Leave>", on_leave)

        poster_frame.bind("<Button-1>",
                          lambda e, frame=poster_frame, m=movie: on_movie_select(frame, m))

        poster_label = ctk.CTkLabel(poster_frame, text=movie["title"], text_color="white",
                                    wraplength=140, justify="center")
        poster_label.pack(expand=True, fill="both", padx=5, pady=5)

        poster_label.bind("<Button-1>",
                          lambda e, frame=poster_frame, m=movie: on_movie_select(frame, m))

root.mainloop()
