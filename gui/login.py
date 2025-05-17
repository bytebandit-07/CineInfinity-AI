import tkinter as tk
import customtkinter as ctk

def on_button_click():
    print("Button clicked!")

def on_closing():
    print("Window closed")
    root.destroy()

root = ctk.CTk()
root._set_appearance_mode("dark")
root.title("Film Flow")
root.geometry("1280x900")
root.configure(bg="#262626")

# Top welcome section
top_frame = ctk.CTkFrame(root, fg_color="#262626")
top_frame.pack(pady=(30, 10), anchor="w", padx=50)

welcome_text = "Film Flow ▶️"
welcome_label = ctk.CTkLabel(top_frame, text="", font=("anton", 50, "bold"), text_color="#E50914")
welcome_label.pack(anchor="w")

def type_welcome(index=0):
    if index < len(welcome_text):
        welcome_label.configure(text=welcome_text[:index+1])
        root.after(100, lambda: type_welcome(index+1))

type_welcome()

ctk.CTkFrame(top_frame, width=280, height=2, fg_color="#E50914").pack(pady=(10, 2), anchor="w")
ctk.CTkFrame(top_frame, width=280, height=2, fg_color="#E50914").pack(anchor="w")

# Outer and login frame
main_frame = ctk.CTkFrame(root, fg_color="#262626")
main_frame.pack(pady=20)

outer_frame = ctk.CTkFrame(main_frame, width=550, height=570, corner_radius=10, fg_color="#E50914")
outer_frame.pack()

login_frame = ctk.CTkFrame(outer_frame, width=540, height=560, corner_radius=30, fg_color="#222222")
login_frame.pack(padx=5, pady=5)

login_label = ctk.CTkLabel(login_frame, text="USER LOGIN", font=("anton", 28, "bold"), text_color="white")
login_label.pack(pady=(20, 10))

# Username and password input section
form_frame = tk.Frame(login_frame, bg="#222222")
form_frame.pack(pady=(10, 0))

usr_row = tk.Frame(form_frame, bg="#222222")
usr_row.pack(pady=(20, 5), anchor="w", padx=60)
usr_label = tk.Label(usr_row, text="Username", font=("playfair", 23, 'bold'), bg="#222222", fg="#E50914")
usr_label.pack(side="left")
login_text = tk.Entry(usr_row, width=25, fg='white', border=0, bg="#222222", font=("arial", 23))
login_text.pack(side="left", padx=10)

ctk.CTkFrame(form_frame, width=286, height=2, fg_color="#E50914").pack(pady=(0, 10))

pass_row = tk.Frame(form_frame, bg="#222222")
pass_row.pack(pady=(10, 5), anchor="w", padx=60)
pass_label = tk.Label(pass_row, text="Password", font=("playfair", 23, 'bold'), bg="#222222", fg="#E50914")
pass_label.pack(side="left")
password_text = tk.Entry(pass_row, width=25, fg='white', border=0, bg="#222222", font=("arial", 23), show="*")
password_text.pack(side="left", padx=10)

toggle_password_button = ctk.CTkButton(
    pass_row, text="👁️", font=('', 18), command=lambda: toggle_password(), hover_color="#222222",
    width=50, height=40, fg_color="#222222"
)
toggle_password_button.pack(side="left", padx=5)

ctk.CTkFrame(form_frame, width=286, height=2, fg_color="#E50914").pack(pady=(0, 10))

# Login button
def bounce_button():
    # Simulate bounce (just a print for now)
    print("Bounce animation")

Login_button = ctk.CTkButton(
    master=login_frame, text="LOGIN", fg_color="#E50914",
    command=lambda: [bounce_button(), on_button_click()]
)
Login_button.pack(pady=(20, 10))

# OR label
OR_label = tk.Label(login_frame, text="----------OR----------", font=("playfair", 26), bg="#222222", fg="white")
OR_label.pack(pady=10)

# Signup section
signup_frame = tk.Frame(login_frame, bg="#222222")
signup_frame.pack(pady=(10, 10))

Signup_label = tk.Label(signup_frame, text="Don't have an account? ", bg="#222222", fg="white", font=("playfair", 23))
Signup_label.pack(side="left")

Signup_button = tk.Button(signup_frame, width=6, text="Sign up", font=("playfair", 23), border=0, bg="#222222",
                          cursor="hand2", fg="#57a1f8")
Signup_button.pack(side="left")

# About us at bottom right
about_container = tk.Frame(root, bg="#262626")
about_container.pack(side="bottom", fill="x", pady=10)

about_button = tk.Button(about_container, width=10, text=" About us ℹ️", font=("playfair", 13),
                         border=0, bg="#262626", cursor="hand2", fg="#57a1f8")
about_button.pack(side="right", padx=20)


def toggle_password():
    if password_text.cget("show") == "*":
        password_text.config(show="")
    else:
        password_text.config(show="*")

root.protocol("WM_DELETE_WINDOW", on_closing)
root.mainloop()
