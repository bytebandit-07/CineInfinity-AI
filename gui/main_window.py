import tkinter as tk

def search_movie():
    movie = entry.get()
    result_label.config(text=f"Searching for recommendations based on: {movie}")

root = tk.Tk()
root.title("CineInfinity AI - Movie Recommender")

tk.Label(root, text="Enter Movie Name:").pack()
entry = tk.Entry(root)
entry.pack()

tk.Button(root, text="Get Recommendations", command=search_movie).pack()
result_label = tk.Label(root, text="")
result_label.pack()

root.mainloop()
