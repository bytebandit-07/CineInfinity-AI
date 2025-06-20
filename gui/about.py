import customtkinter as ctk
import webbrowser
from PIL import Image
import tkinter as tk
import os


def show_about_window(parent):
    """
    Displays the 'About Us' window with developer profiles.

    Args:
        parent (tk.Tk or ctk.CTk): The parent window, which will be hidden.
    """

    def open_link(url):
        """Opens the given URL in a new web browser tab."""
        webbrowser.open_new(url)

    def on_closing():
        """Destroys the 'About Us' window and re-displays the parent window."""
        about_window.destroy()
        parent.deiconify()

    # --- Window Setup ---
    about_window = ctk.CTkToplevel(parent)
    about_window.title("About Us")
    about_window.geometry('1250x600')
    about_window.resizable(False, False)
    about_window.protocol("WM_DELETE_WINDOW", on_closing)
    # The new window should grab focus from the main app
    about_window.transient(parent)
    about_window.grab_set()

    # --- Asset Path Configuration (Robust Method) ---
    try:
        # Assumes this file is in 'gui/' and 'Assets/' is in the root project folder
        _SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
        _ASSETS_DIR = os.path.join(_SCRIPT_DIR, os.pardir, "Assets")
        about_window.iconbitmap(os.path.join(_ASSETS_DIR, "labeel.ico"))
    except tk.TclError:
        print("Warning: Could not load window icon.")
    except FileNotFoundError:
        print("Warning: Assets directory or icon file not found.")

    # --- Main Layout ---
    # Use .pack() for the main sections to ensure they stack vertically without conflict.
    header_label = ctk.CTkLabel(about_window, text="DEVELOPERS", text_color='white', font=('Terminal', 45, 'bold'))
    header_label.pack(pady=(40, 30))

    container = ctk.CTkFrame(about_window, fg_color="transparent")
    container.pack(pady=20, padx=20, expand=True, fill="x")

    # Configure the grid inside the container to space out the developer frames evenly
    container.grid_columnconfigure((0, 1, 2, 3), weight=1)

    # --- Developer Information ---
    developers = [
        {"name": "M Umar Nasir", "image": "Omi.jpg", "link": "https://github.com/omidrogado"},
        {"name": "M Talha Aamir", "image": "Talha.jpg", "link": "https://github.com/NotTonyStarkk-99"},
        {"name": "M Talal", "image": "Talal.jpg", "link": "https://github.com/bytebandit-07"},
        {"name": "Ashir Bin Hamid", "image": "Ashir.jpg", "link": "https://github.com/Lordshadow-afk"}
    ]

    for i, dev in enumerate(developers):
        # Create a frame for each developer
        dev_frame = ctk.CTkFrame(container, fg_color='#333333', width=250, height=370, corner_radius=50)
        dev_frame.grid(row=0, column=i, padx=20)
        dev_frame.pack_propagate(False)

        # Developer Image with Error Handling
        try:
            img_path = os.path.join(_ASSETS_DIR, dev["image"])
            dev_image = ctk.CTkImage(Image.open(img_path), size=(200, 200))
            img_label = ctk.CTkLabel(dev_frame, image=dev_image, text="")
        except FileNotFoundError:
            # If image is not found, display a placeholder
            img_label = ctk.CTkLabel(dev_frame, text="Image Not Found", width=200, height=200, fg_color="#555555")

        img_label.pack(pady=(35, 15))

        # Developer Name and Link
        def create_link_callback(url):
            return lambda e: open_link(url)

        name_label = ctk.CTkLabel(dev_frame, text=dev["name"], text_color="white", font=('Arial', 18, 'bold'),
                                  cursor="hand2")
        name_label.pack(pady=(10, 0))
        name_label.bind("<Button-1>", create_link_callback(dev["link"]))