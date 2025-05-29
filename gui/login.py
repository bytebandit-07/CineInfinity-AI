import tkinter as tk
import customtkinter as ctk
from about import show_about_window
from PIL import Image
from database.db_manager import auth_user


# Functionality of login button
def on_button_click():
    username = login_text.get()
    password = password_text.get()

    if auth_user(username, password):
        root.destroy()  
        import main_window
    else:
        from tkinter import messagebox
        messagebox.showerror("Login Failed", "Invalid username or password")

# Function to handle window close event
def on_closing():
    print("Window closed")  # Log closing event
    root.destroy()  # Properly terminate the application

def open_about_us():
    root.withdraw()  # Hide login window
    import about  # This will show the About Us window
    about.show_about_window(root)


root = ctk.CTk()
root._set_appearance_mode("dark")
root.title("Film Flow")
root.geometry("1280x900")
root.configure(bg="#262626")
root.iconbitmap("../Assets/labeel.ico")


welcome_text = "Film Flow ▶️"
welcome_label = ctk.CTkLabel(root, text="", font=("anton", 50, "bold"), text_color="#E50914")
welcome_label.place(x=50, y=30)

# Welcome animation
def type_welcome(index=0):
    if index < len(welcome_text):
        welcome_label.configure(text=welcome_text[:index+1])
        root.after(100, lambda: type_welcome(index+1))

type_welcome()  # Start the typing animation


under_frame1 = ctk.CTkFrame(root, width=280, height=2, fg_color="#E50914").place(x=50, y=80)
under_frame2 = ctk.CTkFrame(root, width=280, height=2, fg_color="#E50914").place(x=50, y=90)


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


usr_label = tk.Label(login_frame, text="Username", font=("playfair", 23, 'bold'), bg="#222222", fg="#E50914")
usr_label.place(x=62, y=150)

pass_label = tk.Label(login_frame, text="Password", font=("playfair", 23, 'bold'), bg="#222222", fg="#E50914")
pass_label.place(x=67, y=270)


login_text = tk.Entry(login_frame, width=25, fg='white', border=0, bg="#222222", font=("arial", 23))
login_text.place(x=234, y=144)

password_text = tk.Entry(login_frame, width=25, fg='white', border=0, bg="#222222", font=("arial", 23), show="*")
password_text.place(x=230, y=270)


under_frame3 = ctk.CTkFrame(login_frame, width=284, height=2, fg_color="#E50914").place(x=157, y=123)
under_frame4 = ctk.CTkFrame(login_frame, width=286, height=2, fg_color="#E50914").place(x=155, y=208)


# Bounce button animation
def bounce_button():
    original_y = 265
    for offset in [0, -5, -10, -5, 0]:
        Login_button.place(x=210, y=original_y + offset)
        root.update()
        root.after(30)


Login_button = ctk.CTkButton(
    master=login_frame, text="LOGIN", fg_color="#E50914", command=lambda: [bounce_button(), on_button_click()]
)
Login_button.place(x=210, y=265)


OR_label = tk.Label(login_frame, text="----------OR----------", font=("playfair", 26), bg="#222222", fg="white")
OR_label.place(x=255, y=510)


Signup_label = tk.Label(login_frame, text="Don't have an account? ", bg="#222222", fg="white", font=("playfair", 23))
Signup_label.place(x=85, y=620)


Signup_button = tk.Button(login_frame, width=6, text="Sign up", font=("playfair", 23), border=0, bg="#222222", cursor="hand2", fg="#57a1f8")
Signup_button.place(x=410, y=612)
def open_register():
    import register
    register.show_register_window(root)

Signup_button.config(command=open_register)



about_button = tk.Button(login_frame, width=10, text=" About us ℹ️", font=("playfair", 13), border=0, bg="#222222", cursor="hand2", fg="#57a1f8")
about_button.place(x=700, y=790)
about_button.config(command=open_about_us)


# Function to toggle password visibility
def toggle_password():
    if password_text.cget("show") == "*":
        password_text.config(show="")  # Show password
    else:
        password_text.config(show="*")  # Hide password



toggle_password_button = ctk.CTkButton(
    master=login_frame, text="👁️",font=('',18), command=toggle_password,hover_color="#222222", width=50, height=40, fg_color="#222222"
)
toggle_password_button.place(x=450, y=175)

# Add close event handler
root.protocol("WM_DELETE_WINDOW", on_closing)  #


root.mainloop()
