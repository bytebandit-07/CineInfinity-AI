import tkinter as tk
import customtkinter as ctk
from PIL import Image, ImageTk
from ctypes import windll

# Enhanced movie data with more details and genres
movie_categories = {
    "Recommended for you": [
        {"title": "The Shawshank Redemption", "image": "placeholder.jpg",
         "rating": "9.3", "genre": "Drama",
         "description": "Two imprisoned men bond over a number of years, finding solace and eventual redemption through acts of common decency."},
        {"title": "The Godfather", "image": "placeholder.jpg",
         "rating": "9.2", "genre": "Crime",
         "description": "The aging patriarch of an organized crime dynasty transfers control to his reluctant son."},
        {"title": "The Dark Knight", "image": "placeholder.jpg",
         "rating": "9.0", "genre": "Action",
         "description": "When the menace known as the Joker wreaks havoc and chaos on the people of Gotham, Batman must accept one of the greatest psychological and physical tests of his ability to fight injustice."},
        {"title": "Pulp Fiction", "image": "placeholder.jpg",
         "rating": "8.9", "genre": "Crime",
         "description": "The lives of two mob hitmen, a boxer, a gangster and his wife, and a pair of diner bandits intertwine in four tales of violence and redemption."},
        {"title": "Fight Club", "image": "placeholder.jpg",
         "rating": "8.8", "genre": "Drama",
         "description": "An insomniac office worker and a devil-may-care soapmaker form an underground fight club that evolves into something much, much more."},
        {"title": "Inception", "image": "placeholder.jpg",
         "rating": "8.8", "genre": "Sci-Fi",
         "description": "A thief who steals corporate secrets through the use of dream-sharing technology is given the inverse task of planting an idea into the mind of a C.E.O."},
        {"title": "The Matrix", "image": "placeholder.jpg",
         "rating": "8.7", "genre": "Sci-Fi",
         "description": "A computer hacker learns from mysterious rebels about the true nature of his reality and his role in the war against its controllers."},
    ],
    "Trending Now": [
        {"title": "Dune", "image": "placeholder.jpg",
         "rating": "8.0", "genre": "Sci-Fi",
         "description": "Feature adaptation of Frank Herbert's science fiction novel about the son of a noble family entrusted with the protection of the most valuable asset in the galaxy."},
        {"title": "No Time to Die", "image": "placeholder.jpg",
         "rating": "7.3", "genre": "Action",
         "description": "James Bond has left active service. His peace is short-lived when Felix Leiter, an old friend from the CIA, turns up asking for help."},
        {"title": "Spider-Man: No Way Home", "image": "placeholder.jpg",
         "rating": "8.3", "genre": "Action",
         "description": "With Spider-Man's identity now revealed, Peter asks Doctor Strange for help. When a spell goes wrong, dangerous foes from other worlds start to appear."},
        {"title": "The Batman", "image": "placeholder.jpg",
         "rating": "7.9", "genre": "Action",
         "description": "When a sadistic serial killer begins murdering key political figures in Gotham, Batman is forced to investigate the city's hidden corruption."},
        {"title": "Shang-Chi", "image": "placeholder.jpg",
         "rating": "7.4", "genre": "Action",
         "description": "Shang-Chi, the master of weaponry-based Kung Fu, is forced to confront his past after being drawn into the Ten Rings organization."},
        {"title": "Eternals", "image": "placeholder.jpg",
         "rating": "6.3", "genre": "Sci-Fi",
         "description": "The saga of the Eternals, a race of immortal beings who lived on Earth and shaped its history and civilizations."},
        {"title": "Black Widow", "image": "placeholder.jpg",
         "rating": "6.7", "genre": "Action",
         "description": "Natasha Romanoff confronts the darker parts of her ledger when a dangerous conspiracy with ties to her past arises."},
    ],
    "Comedy Movies": [
        {"title": "The Hangover", "image": "placeholder.jpg",
         "rating": "7.7", "genre": "Comedy",
         "description": "Three buddies wake up from a bachelor party in Las Vegas, with no memory of the previous night and the bachelor missing. They make their way around the city in order to find their friend before his wedding."},
        {"title": "Superbad", "image": "placeholder.jpg",
         "rating": "7.6", "genre": "Comedy",
         "description": "Two co-dependent high school seniors are forced to deal with separation anxiety after their plan to stage a booze-soaked party goes awry."},
        {"title": "Bridesmaids", "image": "placeholder.jpg",
         "rating": "6.8", "genre": "Comedy",
         "description": "Competition between the maid of honor and a bridesmaid, over who is the bride's best friend, threatens to upend the life of an out-of-work pastry chef."},
        {"title": "Step Brothers", "image": "placeholder.jpg",
         "rating": "6.9", "genre": "Comedy",
         "description": "Two aimless middle-aged losers still living at home are forced against their will to become roommates when their parents marry."},
        {"title": "Anchorman", "image": "placeholder.jpg",
         "rating": "7.2", "genre": "Comedy",
         "description": "Ron Burgundy is San Diego's top-rated newsman in the male-dominated broadcasting of the 1970s, but that's all about to change when a new female employee arrives."},
        {"title": "The 40-Year-Old Virgin", "image": "placeholder.jpg",
         "rating": "7.1", "genre": "Comedy",
         "description": "Goaded by his buddies, a nerdy guy who's never 'done the deed' only finds the pressure mounting when he meets a single mother."},
        {"title": "Ted", "image": "placeholder.jpg",
         "rating": "6.9", "genre": "Comedy",
         "description": "John Bennett, a man whose childhood wish of bringing his teddy bear to life came true, now must decide between keeping the relationship with the bear or his girlfriend, Lori."},
    ]
}
def showdashboard(user_id):
    # Create main window
    root = ctk.CTk()
    ctk.set_appearance_mode("dark")
    root.geometry("900x600")
    root.title("Film Flow")

    try:
        root.iconbitmap("../Assets/labeel.ico")
    except:
        pass

    # --- Top Menu Frame ---
    menu_frame = ctk.CTkFrame(root, fg_color="#E50914", corner_radius=0)
    menu_frame.pack(fill="x", padx=0, pady=0)

    menu_inner = ctk.CTkFrame(menu_frame, fg_color="#E50914")
    menu_inner.pack(padx=10, pady=10, fill="x")

    title_label = ctk.CTkLabel(menu_inner, text="Film Flow", text_color="white", font=("morganite", 22, "bold"))
    title_label.pack(side="left", padx=(5, 20))

    search_bar = ctk.CTkEntry(menu_inner, placeholder_text="Search", placeholder_text_color="black",
                              width=500, height=30, fg_color="#f0f0f0", text_color="black",
                              border_width=0, corner_radius=150, justify="center")
    search_bar.pack(side="left", padx=(290, 10))

    # --- Main Scrollable Content ---
    content_frame = ctk.CTkScrollableFrame(
        root,
        fg_color="black",
        scrollbar_button_color="#E50914",
        scrollbar_button_hover_color="#B2070F"
    )
    content_frame.pack(fill="both", expand=True)

    # Configure the canvas for smoother scrolling
    content_frame._parent_canvas.configure(highlightthickness=0)
    content_frame._parent_canvas.configure(bg="black")

    selected_movie_frame = None
    detail_window = None


    def show_movie_details(movie_data):
        global detail_window

        # Close previous detail window if it exists
        if detail_window is not None:
            detail_window.destroy()

        # Create new detail window
        detail_window = ctk.CTkToplevel(root)
        detail_window.title(movie_data["title"])
        detail_window.geometry("800x600")
        detail_window.resizable(False, False)
        detail_window.transient(root)  # Set as child of main window
        detail_window.grab_set()  # Make modal

        # Main container
        main_container = ctk.CTkFrame(detail_window, fg_color="black")
        main_container.pack(fill="both", expand=True, padx=20, pady=20)

        # Movie poster (left side)
        poster_frame = ctk.CTkFrame(main_container, width=300, height=450, fg_color="#222222")
        poster_frame.pack_propagate(False)
        poster_frame.pack(side="left", fill="y", padx=(0, 20))

        try:
            img = Image.open(movie_data["image"])
            img = img.resize((300, 450), Image.LANCZOS)
            photo = ImageTk.PhotoImage(img)
        except:
            img = Image.new("RGB", (300, 450), color="gray")
            photo = ImageTk.PhotoImage(img)

        poster_label = tk.Label(poster_frame, image=photo, bg="#222222")
        poster_label.image = photo
        poster_label.pack(expand=True, fill="both")

        # Movie info (right side)
        info_frame = ctk.CTkFrame(main_container, fg_color="black")
        info_frame.pack(side="left", fill="both", expand=True)

        # Title
        title_label = ctk.CTkLabel(info_frame, text=movie_data["title"],
                                   text_color="white", font=("Arial", 28, "bold"),
                                   anchor="w", justify="left")
        title_label.pack(fill="x", pady=(0, 10))

        # Rating
        rating_frame = ctk.CTkFrame(info_frame, fg_color="black")
        rating_frame.pack(fill="x", pady=(0, 20))

        rating_stars = ctk.CTkLabel(rating_frame, text="★" * int(float(movie_data["rating"])),
                                    text_color="#E50914", font=("Arial", 16))
        rating_stars.pack(side="left")

        rating_text = ctk.CTkLabel(rating_frame, text=f"{movie_data['rating']}/10",
                                   text_color="white", font=("Arial", 16))
        rating_text.pack(side="left", padx=(10, 0))

        # Genre
        genre_label = ctk.CTkLabel(info_frame, text=f"Genre: {movie_data['genre']}",
                                   text_color="white", font=("Arial", 14))
        genre_label.pack(fill="x", pady=(0, 10))

        # Description
        desc_label = ctk.CTkLabel(info_frame, text=movie_data["description"],
                                  text_color="white", font=("Arial", 14),
                                  wraplength=400, justify="left", anchor="w")
        desc_label.pack(fill="x", pady=(0, 30))

        # Close button
        close_button = ctk.CTkButton(info_frame, text="Close", fg_color="#333333",
                                     hover_color="#444444", command=detail_window.destroy)
        close_button.pack(side="bottom", pady=(20, 0))


    def on_movie_select(frame, movie_data):
        global selected_movie_frame

        if selected_movie_frame:
            def on_movie_select(frame, movie_data):
                global selected_movie_frame

                if selected_movie_frame and selected_movie_frame.winfo_exists():
                    selected_movie_frame.configure(border_width=0, fg_color="#333333")

                frame.configure(border_width=2, border_color="#E50914", fg_color="#444444")
                selected_movie_frame = frame

                print(f"Selected movie: {movie_data['title']}")
                show_movie_details(movie_data)

        frame.configure(border_width=2, border_color="#E50914", fg_color="#444444")
        selected_movie_frame = frame

        print(f"Selected movie: {movie_data['title']}")
        show_movie_details(movie_data)


    def create_movie_row(container, movies, category_name):
        # Category label
        category_label = ctk.CTkLabel(container, text=category_name, text_color="white",
                                      font=("Arial", 18, "bold"), anchor="w")
        category_label.pack(fill="x", padx=20, pady=(20, 10))

        # Container for horizontal scrolling
        row_container = ctk.CTkFrame(container, fg_color="black")
        row_container.pack(fill="x", padx=20, pady=(0, 20))

        # Canvas and scrollbar for horizontal scrolling
        canvas = tk.Canvas(row_container, bg="black", height=350, highlightthickness=0)
        h_scroll = tk.Scrollbar(row_container, orient="horizontal", command=canvas.xview)

        # Pack scrollbar and canvas
        h_scroll.pack(side="bottom", fill="x")
        canvas.pack(side="top", fill="both", expand=True)
        canvas.configure(xscrollcommand=h_scroll.set)

        # Frame inside canvas for movie posters
        movie_row = ctk.CTkFrame(canvas, fg_color="black")
        canvas.create_window((0, 0), window=movie_row, anchor="nw", tags="movie_row")

        # Configure resizing
        def _on_configure(event, canvas=canvas):
            canvas.configure(scrollregion=canvas.bbox("all"))
            canvas.itemconfigure("movie_row", width=event.width)

        canvas.bind("<Configure>", _on_configure)

        # Add movie posters
        for movie in movies:
            poster_frame = ctk.CTkFrame(movie_row, width=150, height=220,
                                        fg_color="#333333", corner_radius=10)
            poster_frame.pack_propagate(False)
            poster_frame.pack(side="left", padx=10)

            # Hover effects
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

            # Image frame
            image_frame = ctk.CTkFrame(poster_frame, fg_color="black", width=140, height=160)
            image_frame.pack_propagate(False)
            image_frame.pack(fill="x", padx=5, pady=(5, 2))

            try:
                img = Image.open(movie["image"])
                img = img.resize((140, 160), Image.LANCZOS)
                photo = ImageTk.PhotoImage(img)
            except:
                img = Image.new("RGB", (140, 160), color="gray")
                photo = ImageTk.PhotoImage(img)

            image_label = tk.Label(image_frame, image=photo, bg="black")
            image_label.image = photo
            image_label.pack(expand=True, fill="both")
            image_label.bind("<Button-1>",
                             lambda e, frame=poster_frame, m=movie: on_movie_select(frame, m))

            # Title frame
            title_frame = ctk.CTkFrame(poster_frame, fg_color="#333333")
            title_frame.pack(fill="x", padx=5, pady=(2, 5))

            title_label = ctk.CTkLabel(title_frame, text=movie["title"], text_color="white",
                                       font=("Arial", 12), wraplength=130, justify="center")
            title_label.pack(expand=True, fill="both")
            title_label.bind("<Button-1>",
                             lambda e, frame=poster_frame, m=movie: on_movie_select(frame, m))

        return row_container


    def clear_content_frame():
        for widget in content_frame.winfo_children():
            widget.destroy()


    def show_all_movies():
        clear_content_frame()
        for category, movies in movie_categories.items():
            create_movie_row(content_frame, movies, category)


    def search_movie(event=None):
        query = search_bar.get().strip().lower()
        if not query:
            show_all_movies()
            return

        clear_content_frame()

        # Search for matching movies
        found_movies = []
        for category, movies in movie_categories.items():
            for movie in movies:
                if (query in movie["title"].lower() or
                        query in movie["genre"].lower() or
                        query in movie["description"].lower()):
                    found_movies.append(movie)

        if found_movies:
            # Group by genre for better organization
            movies_by_genre = {}
            for movie in found_movies:
                genre = movie["genre"]
                if genre not in movies_by_genre:
                    movies_by_genre[genre] = []
                movies_by_genre[genre].append(movie)

            # Display results by genre
            for genre, movies in movies_by_genre.items():
                create_movie_row(content_frame, movies, f"Results for '{query}' in {genre}")
        else:
            # No results found
            no_results = ctk.CTkLabel(content_frame,
                                      text=f"No results found for '{query}'",
                                      text_color="white", font=("Arial", 16))
            no_results.pack(pady=50)


    # Bind search functionality
    search_bar.bind("<Return>", search_movie)


    # Mouse wheel scrolling function
    def _on_mousewheel(event):
        content_frame._parent_canvas.yview_scroll(int(-1 * (event.delta / 40)), "units")


    # Bind mouse wheel to scrollable frame
    content_frame._parent_canvas.bind_all("<MouseWheel>", _on_mousewheel)

    # Initial display of all movies
    show_all_movies()

    root.mainloop()
