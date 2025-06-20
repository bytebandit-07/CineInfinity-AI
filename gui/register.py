import customtkinter as ctk
from gui.question import show_genre_preferences
import os


# No longer need to import 'messagebox' or 'get_connection'
# This file's only job is to get user input and pass it to the next step.

def show_register_window(parent, backend):
    """
    Displays the user registration window.

    Args:
        parent (ctk.CTk): The parent window (the login screen).
        backend (CineInfinityBackend): The application's backend instance.
    """

    def on_continue_click():
        """Validates input and proceeds to the genre selection step."""
        username = entry_username.get().strip()
        password = entry_password.get()
        confirm_password = entry_confirm_password.get()

        # --- Input Validation ---
        if not username or not password or not confirm_password:
            error_label.configure(text="All fields are required.")
            return
        if password != confirm_password:
            error_label.configure(text="Passwords do not match.")
            return
        if len(password) < 4:
            error_label.configure(text="Password must be at least 4 characters long.")
            return

        # Validation passed, clear any previous error messages
        error_label.configure(text="")

        # Hide this window...
        register_window.withdraw()
        # ...and call the next window with ALL required arguments
        show_genre_preferences(register_window, backend, username, password)

    def on_closing():
        """Handles closing the registration window."""
        register_window.destroy()
        parent.deiconify()  # Show the main login window again

    # --- Window Setup ---
    # Hide the login window while registration is active
    parent.withdraw()
    register_window = ctk.CTkToplevel(parent)
    register_window.title("Create Account")
    register_window.geometry("490x620")  # Increased height for new fields
    register_window.resizable(False, False)
    register_window.protocol("WM_DELETE_WINDOW", on_closing)
    register_window.transient(parent)
    register_window.grab_set()

    # Set Icon
    try:
        _SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
        _ASSETS_DIR = os.path.join(_SCRIPT_DIR, os.pardir, "Assets")
        ICON_PATH = os.path.join(_ASSETS_DIR, "labeel.ico")
        register_window.iconbitmap(ICON_PATH)
    except Exception as e:
        print(f"Warning: Could not load register window icon: {e}")

    # --- UI Layout (Adapted from your code) ---
    frame = ctk.CTkFrame(register_window, fg_color="#333333", corner_radius=15)
    frame.pack(pady=50, padx=50, fill="both", expand=True)

    label_title = ctk.CTkLabel(frame, text="Sign Up", font=("Arial", 28, "bold"), text_color="white")
    label_title.pack(pady=(20, 30))

    # Username Entry
    ctk.CTkLabel(frame, text="Username", font=("Arial", 12), text_color="gray").pack(anchor="w", padx=45)
    entry_username = ctk.CTkEntry(frame, placeholder_text="Choose a unique username", width=300, height=40)
    entry_username.pack(pady=(5, 15))

    # Password Entry
    ctk.CTkLabel(frame, text="Password", font=("Arial", 12), text_color="gray").pack(anchor="w", padx=45)
    entry_password = ctk.CTkEntry(frame, placeholder_text="Create a password", show="*", width=300, height=40)
    entry_password.pack(pady=(5, 15))

    # Confirm Password Entry (Essential for good UX)
    ctk.CTkLabel(frame, text="Confirm Password", font=("Arial", 12), text_color="gray").pack(anchor="w", padx=45)
    entry_confirm_password = ctk.CTkEntry(frame, placeholder_text="Confirm your password", show="*", width=300,
                                          height=40)
    entry_confirm_password.pack(pady=5)

    # Error Label to show validation messages
    error_label = ctk.CTkLabel(frame, text="", text_color="#FF5555", font=("Arial", 12))
    error_label.pack(pady=10)

    # Button to proceed
    btn_continue = ctk.CTkButton(frame, text="Continue", command=on_continue_click, width=300, height=40,
                                 fg_color="#E50914", hover_color="#C40812")
    btn_continue.pack(pady=20)