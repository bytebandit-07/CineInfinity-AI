import tkinter as tk
import customtkinter as ctk
# Corrected import: use the full path if 'about.py' is not in the same directory
# Assuming 'about.py' is in a 'gui' subdirectory relative to 'main.py' (or 'login.py')
# If 'about.py' is in the same directory as login.py, then 'from about import show_about_window' is fine.
# Let's assume it's in a 'gui' folder if your structure is similar to the main_window.py example
from gui.about import show_about_window # Assuming gui/about.py

from PIL import Image
from backend.app import CineInfinityBackend # Import CineInfinityBackend
import os

# Initialize backend globally or pass it around as needed
# It's good practice to initialize it once for the application lifecycle
backend = CineInfinityBackend()

# Functionality of login button
def on_login_click(): # Renamed to avoid confusion with the widget
    username = login_text.get()
    password = password_text.get()

    if backend.login(username, password): # Use the backend's login method
        root.destroy()
        # Ensure you import and call the correct main window function
        # Based on your previous snippet, show_main from main_window.py
        from gui.main_window import show_main
        show_main(backend, username) # Pass the backend instance and username
    else:
        # Instead of messagebox, update the error_label in the form
        error_label.configure(text="Invalid credentials - Try again")


# Function to handle window close event
def on_closing():
    print("Window closed")  # Log closing event
    root.destroy()  # Properly terminate the application

def open_about_us():
    root.withdraw()  # Hide login window
    # Corrected call: Pass the root window as the parent
    show_about_window(root)


_SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
_ASSETS_DIR = os.path.join(_SCRIPT_DIR, os.pardir, "Assets")
ICON_PATH = os.path.join(_ASSETS_DIR, "labeel.ico")

root = ctk.CTk()
ctk.set_appearance_mode("dark") # Use ctk.set_appearance_mode directly
root.title("Film Flow")
root.geometry("1280x900")
root.configure(bg="#262626")
try:
    root.iconbitmap(ICON_PATH)
except tk.TclError:
    print(f"Warning: Could not load icon from {ICON_PATH}")
    # Fallback if icon isn't found or platform doesn't support .ico


welcome_text = "Film Flow ▶️"
welcome_label = ctk.CTkLabel(root, text="", font=("anton", 50, "bold"), text_color="#E50914")
welcome_label.place(x=50, y=30)

# Welcome animation
def type_welcome(index=0):
    if index < len(welcome_text):
        welcome_label.configure(text=welcome_text[:index+1])
        root.after(100, lambda: type_welcome(index+1))

type_welcome()  # Start the typing animation


under_frame1 = ctk.CTkFrame(root, width=280, height=2, fg_color="#E50914")
under_frame1.place(x=50, y=80)
under_frame2 = ctk.CTkFrame(root, width=280, height=2, fg_color="#E50914")
under_frame2.place(x=50, y=90)


outer_frame = ctk.CTkFrame(root,
                           width=550, height=570,
                           corner_radius=10,
                           fg_color="#E50914")
outer_frame.place(x=690, y=75)


login_frame = ctk.CTkFrame(outer_frame,
                           width=540, height=560,
                           corner_radius=30,
                           fg_color="#222222")
login_frame.place(x=5, y=5)


login_label = ctk.CTkLabel(login_frame, text="USER LOGIN", font=("anton", 28, "bold"), text_color="white")
login_label.place(x=186, y=25)


usr_label = ctk.CTkLabel(login_frame, text="Username", font=("playfair", 23, 'bold'), text_color="#E50914") # Use CTkLabel
usr_label.place(x=62, y=150)

pass_label = ctk.CTkLabel(login_frame, text="Password", font=("playfair", 23, 'bold'), text_color="#E50914") # Use CTkLabel
pass_label.place(x=67, y=270)


login_text = ctk.CTkEntry(login_frame, width=250, fg_color="#1A1A1A", text_color="white", border_width=0, font=("arial", 23)) # Use CTkEntry
login_text.place(x=234, y=144)

password_text = ctk.CTkEntry(login_frame, width=250, fg_color="#1A1A1A", text_color="white", border_width=0, font=("arial", 23), show="*") # Use CTkEntry
password_text.place(x=230, y=270)


under_frame3 = ctk.CTkFrame(login_frame, width=284, height=2, fg_color="#E50914")
under_frame3.place(x=157, y=183) # Adjusted y-coordinate to be below entry, not on top of it.
under_frame4 = ctk.CTkFrame(login_frame, width=286, height=2, fg_color="#E50914")
under_frame4.place(x=155, y=318) # Adjusted y-coordinate


# Error label for login
error_label = ctk.CTkLabel(login_frame, text="", font=("Helvetica",12), text_color="#FF5555")
error_label.place(x=186, y=340) # Place it below password field


# Bounce button animation
def bounce_button(button_widget):
    original_y = button_widget.winfo_y()
    original_x = button_widget.winfo_x()
    for offset in [0, -5, -10, -5, 0]:
        button_widget.place(x=original_x, y=original_y + offset)
        root.update_idletasks() # Update the window
        root.after(30)


Login_button = ctk.CTkButton(
    master=login_frame, text="LOGIN", fg_color="#E50914", hover_color="#C40812",
    font=("Helvetica",16,"bold"), height=50, corner_radius=8,
    command=lambda: [bounce_button(Login_button), on_login_click()] # Pass the button to bounce_button
)
Login_button.place(x=140, y=370, width=280) # Adjusted placement and width


OR_label = ctk.CTkLabel(login_frame, text="----------OR----------", font=("playfair", 20), text_color="white") # Use CTkLabel
OR_label.place(x=160, y=430) # Adjusted placement


Signup_label = ctk.CTkLabel(login_frame, text="Don't have an account? ", text_color="white", font=("playfair", 18)) # Use CTkLabel
Signup_label.place(x=90, y=470)


Signup_button = ctk.CTkButton(login_frame, text="Sign up", font=("playfair", 18, "underline"), fg_color="transparent",
                              hover_color="#222222", text_color="#57a1f8", cursor="hand2")
Signup_button.place(x=300, y=470) # Adjusted placement
def open_register():
    # It's better to pass the root window to register for back button functionality
    root.withdraw()
    from gui.register import show_register_window # Assuming gui/register.py
    show_register_window(root)

Signup_button.config(command=open_register)


about_button = ctk.CTkButton(login_frame, text="About us ℹ️", font=("playfair", 13), fg_color="transparent",
                             hover_color="#222222", text_color="#777777", cursor="hand2")
about_button.place(relx=0.5, rely=0.95, anchor="center") # Centered relative to login_frame
about_button.config(command=open_about_us)


# Function to toggle password visibility
def toggle_password():
    if password_text.cget("show") == "*":
        password_text.configure(show="")  # Show password
    else:
        password_text.configure(show="*")  # Hide password


toggle_password_button = ctk.CTkButton(
    master=login_frame, text="👁️",font=('',18), command=toggle_password,hover_color="#222222",
    width=30, height=28, fg_color="transparent", # Adjusted size for eye icon
    text_color="#AAAAAA" # Added text color for the eye icon
)
toggle_password_button.place(x=490, y=278) # Adjusted position for eye icon


# Add close event handler
root.protocol("WM_DELETE_WINDOW", on_closing)

root.mainloop()