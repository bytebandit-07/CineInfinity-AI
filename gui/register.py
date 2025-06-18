import customtkinter as ctk
from tkinter import messagebox
from database.db_manager import register_user
from question import show_genre_preferences

def show_register_window(parent):
    def sign_in():
        username = entry_username.get()
        password = entry_password.get()

        result = register_user(username, password)

        if result == "existed":
            messagebox.showerror("Error", "User already exists")
        elif result is True:
            messagebox.showinfo("Success", "Welcome to the hood 😎")
            register_window.destroy()
            show_genre_preferences()
        else:
            messagebox.showerror("Error", "Failed to register user")


    def on_closing():
        register_window.destroy()
        parent.deiconify()  # Show login window again

    ctk.set_appearance_mode("dark")

    parent.withdraw()  # Hide the login window
    register_window = ctk.CTkToplevel()
    register_window.title("Sign in")
    register_window.geometry("490x590")
    register_window.iconbitmap("../Assets/labeel.ico")
    register_window.resizable(False, False)
    register_window.protocol("WM_DELETE_WINDOW", on_closing)


    frame = ctk.CTkFrame(register_window, fg_color="#333333", corner_radius=15)
    frame.pack(pady=100, padx=50, fill="both", expand=False)

    label_title = ctk.CTkLabel(frame, text="Sign In", font=("Arial", 24, "bold"), text_color="white")
    label_title.pack(pady=20)

    entry_username = ctk.CTkEntry(frame, placeholder_text="Username", width=300)
    entry_username.pack(pady=10)

    entry_password = ctk.CTkEntry(frame, placeholder_text="Password", width=300)
    entry_password.pack(pady=10)

    btn_signin = ctk.CTkButton(frame, text="Sign In", command=sign_in, width=300, fg_color="#E50914")
    btn_signin.pack(pady=20)
