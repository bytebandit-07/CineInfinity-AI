import tkinter as tk
import customtkinter as ctk
from PIL import Image, ImageTk
from database.db_manager import auth_user

# Functionality
def on_button_click():
    username = login_text.get()
    password = password_text.get()

    if auth_user(username, password):
        root.destroy()
        import main_window
    else:
        error_label.configure(text="Invalid credentials - Try again", text_color="#FF5555")

        try:
            password_text.delete(0, 'end')
            # Temporarily increase border width for visibility
            login_text.configure(border_color="#FF5555", border_width=2)
            password_text.configure(border_color="#FF5555", border_width=2)

            # Force redraw
            login_text.update_idletasks()
            password_text.update_idletasks()
        except Exception as e:
            print("Warning: Entry widgets do not support border_color:", e)


def on_closing():
    root.destroy()

def toggle_password():
    if password_text.cget('show') == '':
        password_text.configure(show='*')
        toggle_btn.configure(text='👁️')
    else:
        password_text.configure(show='')
        toggle_btn.configure(text='🔒')

def on_entry_click(event):
    widget = event.widget
    if isinstance(widget, ctk.CTkEntry):
        widget.configure(border_color="#E50914")
        error_label.configure(text="")

def on_entry_leave(event):
    widget = event.widget
    if isinstance(widget, ctk.CTkEntry):
        widget.configure(border_color="#333333")


def open_about_us():
    root.withdraw()
    import about
    about.show_about_window(root)

def open_register():
    root.withdraw()
    import register
    register.show_register_window(root)

# Main window setup
root = ctk.CTk()
root._set_appearance_mode("dark")
root.title("Film Flow - Login")
root.geometry("1200x750")
root.configure(bg="#0A0A0A")

# Background - Film Strip Effect
bg_frame = ctk.CTkFrame(root, fg_color="#0A0A0A")
bg_frame.pack(fill="both", expand=True)

# Left side - Movie Poster Carousel
poster_frame = ctk.CTkFrame(bg_frame, fg_color="transparent", width=500)
poster_frame.pack(side="left", fill="y", padx=20)

# Sample movie posters (replace with actual images)
posters = [
    "../Assets/poster1.jpg",  # Replace with actual paths
    "../Assets/poster2.jpg",
    "../Assets/poster3.jpg"
]

# For demo purposes, we'll use colored placeholders
for i in range(3):
    poster = ctk.CTkFrame(poster_frame,
                         width=300,
                         height=450,
                         corner_radius=12,
                         fg_color="#1A1A1A",
                         border_width=2,
                         border_color="#333333")
    poster.pack(pady=15)
    label = ctk.CTkLabel(poster,
                        text=f"Movie Poster {i+1}",
                        font=("Helvetica", 14),
                        text_color="#777777")
    label.pack(expand=True)

# Right side - Login Form
login_container = ctk.CTkFrame(bg_frame,
                             width=600,
                             corner_radius=20,
                             fg_color="#111111",
                             border_width=1,
                             border_color="#222222")
login_container.pack(side="right", fill="both", expand=True, padx=40, pady=40)

# App Logo/Title
logo_frame = ctk.CTkFrame(login_container, fg_color="transparent")
logo_frame.pack(pady=(50, 30))

app_logo = ctk.CTkLabel(logo_frame,
                       text="🎬 FILM FLOW",
                       font=("Impact", 42),
                       text_color="#E50914")
app_logo.pack()

tagline = ctk.CTkLabel(logo_frame,
                      text="Your Personal Movie Curator",
                      font=("Helvetica", 16),
                      text_color="#888888")
tagline.pack(pady=(5, 0))

# Form container
form_frame = ctk.CTkFrame(login_container, fg_color="transparent")
form_frame.pack(pady=(0, 20), padx=80, fill="x")

# Username field
username_frame = ctk.CTkFrame(form_frame, fg_color="transparent")
username_frame.pack(pady=(0, 20), fill="x")

ctk.CTkLabel(username_frame,
            text="USERNAME",
            font=("Helvetica", 12, "bold"),
            text_color="#AAAAAA").pack(anchor="w")

login_text = ctk.CTkEntry(username_frame,
                        placeholder_text="Enter your username",
                        font=("Helvetica", 15),
                        height=48,
                        fg_color="#1A1A1A",
                        border_width=1,
                        border_color="#333333",
                        corner_radius=8)
login_text.pack(fill="x", pady=(5, 0))
login_text.bind("<FocusIn>", on_entry_click)
login_text.bind("<FocusOut>", on_entry_leave)

# Password field
password_frame = ctk.CTkFrame(form_frame, fg_color="transparent")
password_frame.pack(pady=(0, 10), fill="x")

password_top = ctk.CTkFrame(password_frame, fg_color="transparent")
password_top.pack(fill="x")

ctk.CTkLabel(password_top,
            text="PASSWORD",
            font=("Helvetica", 12, "bold"),
            text_color="#AAAAAA").pack(side="left")

# Toggle password button
toggle_btn = ctk.CTkButton(password_top,
                         text="👁️",
                         width=30,
                         height=28,
                         fg_color="transparent",
                         hover_color="#222222",
                         command=toggle_password)
toggle_btn.pack(side="right")

password_text = ctk.CTkEntry(password_frame,
                           placeholder_text="Enter your password",
                           font=("Helvetica", 15),
                           show="*",
                           height=48,
                           fg_color="#1A1A1A",
                           border_width=1,
                           border_color="#333333",
                           corner_radius=8)
password_text.pack(fill="x", pady=(5, 0))
password_text.bind("<FocusIn>", on_entry_click)
password_text.bind("<FocusOut>", on_entry_leave)

# Error label
error_label = ctk.CTkLabel(form_frame, text="", font=("Helvetica", 12))
error_label.pack(pady=(5, 0))

# Login button
Login_button = ctk.CTkButton(form_frame,
                           text="START STREAMING",
                           fg_color="#E50914",
                           hover_color="#C40812",
                           font=("Helvetica", 16, "bold"),
                           height=50,
                           corner_radius=8,
                           command=on_button_click)
Login_button.pack(pady=30, fill="x")

# Footer
footer_frame = ctk.CTkFrame(login_container, fg_color="transparent")
footer_frame.pack(fill="x", pady=(0, 40), padx=80)

ctk.CTkLabel(footer_frame,
            text="New to Film Flow?",
            font=("Helvetica", 13),
            text_color="#777777").pack(side="left", padx=(0, 5))

signup_btn = ctk.CTkButton(footer_frame,
                          text="Create Account",
                          fg_color="transparent",
                          hover_color="#222222",
                          font=("Helvetica", 13, "underline"),
                          text_color="#57a1f8",
                          command=open_register,
                          anchor="w")
signup_btn.pack(side="left")

about_btn = ctk.CTkButton(footer_frame,
                         text="About Us",
                         fg_color="transparent",
                         hover_color="#222222",
                         font=("Helvetica", 13),
                         text_color="#777777",
                         command=open_about_us)
about_btn.pack(side="right")

root.protocol("WM_DELETE_WINDOW", on_closing)
root.mainloop()