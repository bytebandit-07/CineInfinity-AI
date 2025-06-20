import customtkinter as ctk
# No need to import tkinter as tk if only ctk is used
from PIL import Image


def show_genre_preferences(parent, backend, username, password):
    """
    Displays the genre preference selection window during registration.

    Args:
        parent: The parent window (register window) to hide.
        backend (CineInfinityBackend): The application's backend instance.
        username (str): The new user's username.
        password (str): The new user's password.
    """
    genre_window = ctk.CTkToplevel(parent)
    genre_window.title("What do you like?")
    genre_window.geometry("600x700")
    genre_window.resizable(False, False)
    # Ensure this window takes focus
    genre_window.transient(parent)
    genre_window.grab_set()

    # Center the window relative to the parent
    x = parent.winfo_x() + (parent.winfo_width() // 2) - (600 // 2)
    y = parent.winfo_y() + (parent.winfo_height() // 2) - (700 // 2)
    genre_window.geometry(f"600x700+{x}+{y}")

    def on_submit():
        """Handles the submission of selected genres."""
        selected_genres = [cb.cget("text").split()[0] for cb in checkboxes if cb.get() == 1]

        # Use the backend to register the user
        registration_result = backend.register(username, password, selected_genres)

        if registration_result is True:
            print(f"✅ User '{username}' successfully registered.")
            # Destroy all registration-related windows
            genre_window.destroy()
            parent.destroy()  # This will close the hidden register window

            # Now, show the main login screen
            from gui.main import show_login
            show_login()
        else:
            # Handle registration failure (e.g., user already exists)
            # This part can be enhanced with a CTkMessagebox if you have one
            print(f"❌ Registration failed. Result: {registration_result}")
            # Optionally show an error message on the genre window
            error_label.configure(text=f"Registration failed: {registration_result}")

    # This is a much cleaner way to handle the checkboxes and their colors
    genre_colors = {
        "Horror": "red", "Romance": "#FF69B4", "Action": "#FFD300",
        "Comedy": "#f7ee6d", "Adventure": "#32cd32", "Animation": "#a45ee9",
        "Children": "#45b6fe", "Crime": "red", "Documentary": "#CCCCCC",
        "Drama": "#f7ee6d", "Fantasy": "#BA55D3", "Film-Noir": "#00FFFF",
        "IMAX": "#1E90FF", "Musical": "#FFA500", "Mystery": "#9370DB",
        "Sci-Fi": "#7CFC00", "Thriller": "#FF1493", "War": "#CD5C5C", "Western": "#DEB887"
    }
    genres = list(genre_colors.keys())

    # --- UI LAYOUT ---
    header = ctk.CTkLabel(genre_window, text="Tell us your preferences 🧐", font=('joyous', 32, 'bold'))
    header.pack(pady=(20, 10))

    # Frame to hold the two columns of checkboxes
    selection_frame = ctk.CTkFrame(genre_window, fg_color="transparent")
    selection_frame.pack(pady=10, padx=20, fill="x", expand=True)
    selection_frame.grid_columnconfigure((0, 1), weight=1)

    checkboxes = []
    # Create checkboxes dynamically
    for i, genre in enumerate(genres):
        col = 0 if i < 10 else 1  # Split into two columns

        checkbox = ctk.CTkCheckBox(selection_frame, text=f"{genre} {'💀'}", font=('Arial', 18))
        checkbox.grid(row=i % 10, column=col, padx=20, pady=8, sticky="w")
        checkboxes.append(checkbox)

    # Label for showing registration errors
    error_label = ctk.CTkLabel(genre_window, text="", text_color="red", font=('Arial', 12))
    error_label.pack(pady=(5, 10))

    submit_button = ctk.CTkButton(
        genre_window,
        text='SUBMIT & FINISH',
        font=('Ink Free', 16, 'bold'),
        corner_radius=20,
        height=40,
        fg_color='red',
        hover_color='#C40812',
        command=on_submit
    )
    submit_button.pack(pady=(10, 20))