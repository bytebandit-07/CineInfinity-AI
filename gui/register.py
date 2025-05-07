import customtkinter as ctk 
from tkinter import messagebox  # Import messagebox for pop-ups
from PIL import Image 

# Initialize the application window
ctk.set_appearance_mode("dark")  

root = ctk.CTk()
root.title("Sign in")
root.geometry("490x590")
root.resizable(False, False)



# Create a semi-transparent frame for login UI
frame = ctk.CTkFrame(root, fg_color="#333333", corner_radius=15)  # Dark semi-transparent frame
frame.pack(pady=100, padx=50, fill="both", expand=False)

# Title Label
label_title = ctk.CTkLabel(frame, text="Sign In", font=("Arial", 24, "bold"), text_color="white")
label_title.pack(pady=20)

# Username Entry
entry_username = ctk.CTkEntry(frame, placeholder_text="Username", width=300)
entry_username.pack(pady=10)

# Password Entry
entry_password = ctk.CTkEntry(frame, placeholder_text="Password", width=300)
entry_password.pack(pady=10)

# Sign-in function
def sign_in():
    username = entry_username.get()
    password = entry_password.get()
    
    if username == "admin" and password == "password":  # Dummy credentials
        messagebox.showinfo("Success", "Login Successful!")
    else:
        messagebox.showerror("Error", "Invalid Username or Password")

# Sign-in Button (Linked to sign_in function)
btn_signin = ctk.CTkButton(frame, text="Sign In", command=sign_in, width=300,fg_color="#fda600")
btn_signin.pack(pady=20)

# Handle window close event
def on_closing():
    print("Window closed")
    root.destroy()  

root.protocol("WM_DELETE_WINDOW", on_closing)

root.mainloop()
