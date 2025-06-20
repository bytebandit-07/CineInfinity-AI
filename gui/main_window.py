import customtkinter as ctk
from PIL import Image
from io import BytesIO
import requests


# We are no longer using threading to remove the source of the bug
# import threading

class MainWindow(ctk.CTk):
    def __init__(self, backend, username):
        super().__init__()
        self.backend = backend
        self.username = username
        self.photo_references = []  # Still keeping this as a safety measure

        self.setup_ui()
        self.populate_dashboard()

    def setup_ui(self):
        ctk.set_appearance_mode("dark")
        self.title(f"Film Flow - Welcome, {self.username}")
        self.geometry("1000x700")

        top_frame = ctk.CTkFrame(self, fg_color="#E50914", corner_radius=0)
        top_frame.pack(fill="x")

        ctk.CTkLabel(top_frame, text="Film Flow", font=("Arial", 22, "bold"), text_color="white").pack(side="left",
                                                                                                       padx=20, pady=10)
        self.search_entry = ctk.CTkEntry(top_frame, width=400, placeholder_text="Search for a movie...",
                                         corner_radius=20)
        self.search_entry.pack(side="left", padx=10, pady=10, expand=True)
        self.search_entry.bind("<Return>", lambda e: self.search_and_display())
        ctk.CTkButton(top_frame, text="Search", width=80, corner_radius=20, command=self.search_and_display).pack(
            side="left", padx=(0, 20), pady=10)
        ctk.CTkButton(top_frame, text="Logout", fg_color="#000", hover_color="#111", command=self.do_logout).pack(
            side="right", padx=20, pady=10)

        self.content_frame = ctk.CTkScrollableFrame(self, fg_color="black", scrollbar_button_color="#E50914",
                                                    scrollbar_button_hover_color="#B2070F")
        self.content_frame.pack(fill="both", expand=True)

    def do_logout(self):
        self.destroy()
        from gui.main import show_login
        show_login()

    def show_movie_details(self, movie_info, poster_image=None):
        detail_window = ctk.CTkToplevel(self)
        detail_window.title(movie_info['title'])
        detail_window.geometry("500x600")
        detail_window.transient(self)
        detail_window.grab_set()

        x = self.winfo_x() + (self.winfo_width() // 2) - (500 // 2)
        y = self.winfo_y() + (self.winfo_height() // 2) - (600 // 2)
        detail_window.geometry(f"500x600+{x}+{y}")

        detail_frame = ctk.CTkFrame(detail_window, fg_color="#1A1A1A", corner_radius=10)
        detail_frame.pack(fill="both", expand=True, padx=20, pady=20)

        description = self.backend.get_movie_description(movie_info['title'])

        ctk.CTkLabel(detail_frame, text=movie_info['title'], font=("Arial", 24, "bold"), text_color="#E50914",
                     wraplength=450).pack(pady=(10, 5))
        ctk.CTkLabel(detail_frame, text=f"Genre: {movie_info.get('genres', 'N/A')}", font=("Arial", 14),
                     text_color="#AAAAAA").pack()
        ctk.CTkLabel(detail_frame, text=f"Rating: {movie_info.get('avg_rating', 'N/A')}", font=("Arial", 16, "bold"),
                     text_color="#F5C518").pack(pady=5)

        if poster_image:
            photo = ctk.CTkImage(light_image=poster_image, size=(200, 280))
        else:
            try:
                poster_url = self.backend.get_image_url(movie_info['title'])
                if not poster_url: raise ValueError("No URL")
                resp = requests.get(poster_url, timeout=5)
                resp.raise_for_status()
                img = Image.open(BytesIO(resp.content))
                photo = ctk.CTkImage(light_image=img, size=(200, 280))
            except Exception:
                img = Image.new("RGB", (200, 280), color="#555555")
                photo = ctk.CTkImage(light_image=img, size=(200, 280))

        img_label = ctk.CTkLabel(detail_frame, image=photo, text="")
        img_label.image = photo
        self.photo_references.append(photo)
        img_label.pack(pady=15)

        desc_label = ctk.CTkLabel(detail_frame, text=description, font=("Arial", 14), text_color="white",
                                  wraplength=450, justify="left")
        desc_label.pack(pady=(0, 20), fill="x", expand=True)

        ctk.CTkButton(detail_frame, text="Close", command=detail_window.destroy, fg_color="#E50914",
                      hover_color="#C40812").pack(pady=10)

    # --- SIMPLIFIED create_movie_row FUNCTION (NO MORE THREADING) ---
    def create_movie_row(self, container, movies, category_name):
        ctk.CTkLabel(container, text=category_name, font=("Arial", 18, "bold"), anchor="w").pack(fill="x", padx=20,
                                                                                                 pady=(20, 10))
        row_frame = ctk.CTkScrollableFrame(container, fg_color="black", orientation="horizontal", height=280)
        row_frame.pack(fill="x", padx=10, pady=(0, 20))

        for movie in movies:
            card = ctk.CTkFrame(row_frame, width=150, height=250, corner_radius=8, fg_color="#222222")
            card.pack(side="left", padx=10, pady=10)
            card.pack_propagate(False)

            # Load image directly here. This will be slow but stable.
            try:
                poster_url = self.backend.get_image_url(movie['title'])
                if not poster_url: raise ValueError("No URL")
                resp = requests.get(poster_url, timeout=10)
                resp.raise_for_status()
                pil_img = Image.open(BytesIO(resp.content)).resize((140, 200), Image.LANCZOS)
            except Exception as e:
                print(f"Failed to load poster for {movie['title']}: {e}")
                pil_img = Image.new("RGB", (140, 200), color="#555555")

            photo = ctk.CTkImage(light_image=pil_img, size=(140, 200))
            self.photo_references.append(photo)  # Keep reference

            img_label = ctk.CTkLabel(card, image=photo, text="")
            img_label.image = photo  # Anchor reference
            img_label.pack(pady=(5, 5))

            title_label = ctk.CTkLabel(card, text=movie['title'], wraplength=140, font=("Arial", 12))
            title_label.pack(expand=True, fill="x", padx=5)

            # Bind click event
            card.bind("<Button-1>", lambda e, m=movie, p=pil_img: self.show_movie_details(m, p))
            img_label.bind("<Button-1>", lambda e, m=movie, p=pil_img: self.show_movie_details(m, p))

    def populate_dashboard(self):
        self.clear_content_frame()
        loading_label = ctk.CTkLabel(self.content_frame, text="Loading recommendations, please wait...",
                                     font=("Arial", 18))
        loading_label.pack(pady=50)
        self.update_idletasks()

        user_history = self.backend.get_user_history()
        if user_history:
            recs = self.backend.recommend(user_history[0], 10)
        else:
            # Changed default movie since "The Matrix" was not found
            recs = self.backend.recommend("Inception", 10)

        action_recs = self.backend.recommend("The Dark Knight", 7)
        comedy_recs = self.backend.recommend("Superbad", 7)

        loading_label.destroy()

        if recs: self.create_movie_row(self.content_frame, recs, "Recommended For You")
        if action_recs: self.create_movie_row(self.content_frame, action_recs, "Action & Adventure")
        if comedy_recs: self.create_movie_row(self.content_frame, comedy_recs, "Comedy")

    def search_and_display(self):
        query = self.search_entry.get().strip()
        if not query:
            self.populate_dashboard()
            return
        self.clear_content_frame()
        results = self.backend.recommend(query, 20)
        if results:
            self.create_movie_row(self.content_frame, results, f"Results for '{query}'")
        else:
            ctk.CTkLabel(self.content_frame, text=f"No results found for '{query}'").pack(pady=50)

    def clear_content_frame(self):
        self.photo_references.clear()
        for widget in self.content_frame.winfo_children():
            widget.destroy()


def show_main(backend, username):
    app = MainWindow(backend, username)
    app.mainloop()