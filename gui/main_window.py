import tkinter as tk
import customtkinter as ctk

def search_movie():
    movie = entry.get()
    result_label.config(text=f"Searching for recommendations based on: {movie}")

root = ctk.CTk()
ctk.set_appearance_mode("dark")
root.geometry("900x600")
root.title("Film Flow")

menu_frame=ctk.CTkFrame(root,fg_color="#E50914",width=1400,height=50,corner_radius=False)
menu_frame.place(x=1,y=1)


tk.Label(root, text="Enter Movie Name:").pack(pady=400)
entry = tk.Entry(root)
entry.pack(pady=450)

tk.Button(root, text="Get Recommendations", command=search_movie).pack(pady=600)
result_label = tk.Label(root, text="")
result_label.pack(pady=620)

root.mainloop()
