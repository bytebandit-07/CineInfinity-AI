import tkinter as tk
import customtkinter as ctk


# Functionality of login button
def on_button_click():
    print("Button clicked!")  # Placeholder action
# Function to handle window close event
def on_closing():
    print("Window closed")  # Log closing event
    root.destroy()  # Properly terminate the application


# Initialize the main application window
root = ctk.CTk()
root._set_appearance_mode("dark")  # Set dark mode
root.title("Film Flow")  # Set window title
root.geometry("970x570")  # Set window size
root.configure(bg="#262626")  # Set background color



# Adding welcome text
welcome_label = ctk.CTkLabel(root, text="Welcome to Film Flow 😉", font=("anton",50,"bold"),text_color="white")
welcome_label.place(x=50,y=50)

#adding frame

# Outer frame (Border effect)
outer_frame = ctk.CTkFrame(root, 
                           width=550, height=570,  # Set width & height in constructor
                           corner_radius=10, 
                           fg_color="#6D0C99")  # Border color
outer_frame.place(x=690, y=120)  # Place without width/height


# Inner login frame (Main content)
login_frame = ctk.CTkFrame(outer_frame, 
                           width=540, height=560,  # Set width & height in constructor
                           corner_radius=30, 
                           fg_color="#222222")  # Main frame color
login_frame.place(x=5, y=5)  # Offset inside the outer frame for border effect

#Adding login label
login_label = ctk.CTkLabel(login_frame, text="USER LOGIN", font=("anton",28,"bold"),text_color="white")
login_label.place(x=186,y=25)

# Adding labels for username and password fields
usr_label = tk.Label(login_frame, text="Username", font=("playfair", 23, 'bold'), bg="#890DB7", fg="white")
usr_label.place(x=64, y=150)

pass_label = tk.Label(login_frame, text="Password", font=("playfair", 23, 'bold'), bg="#890DB7", fg="white")
pass_label.place(x=67, y=270)

# Adding input fields for username and password
login_text = tk.Entry(login_frame, width=25, fg='black', border=2, bg="white", font=("arial", 23))
login_text.place(x=230, y=150)

password_text = tk.Entry(login_frame, width=25, fg='black', border=2, bg="white", font=("arial", 23), show="*")
password_text.place(x=230, y=270)



# Create the login button
Login_button = ctk.CTkButton(
    master=login_frame, text="Login", command=on_button_click, width=130, height=40,
    fg_color="#890DB7", hover_color="#0096FF", corner_radius=20, font=("Helvetica", 14)
)
Login_button.place(x=210, y=265)
#Adding OR label
OR_label = tk.Label(login_frame, text="----------OR----------", font=("playfair", 26), bg="#222222", fg="white")
OR_label.place(x=255,y=510)

# Add a label for the sign-up option
Signup_label = tk.Label(login_frame, text="Don't have an account? ", bg="#222222", fg="white", font=("playfair", 23))
Signup_label.place(x=85, y=620)

# Add the sign-up button
Signup_button = tk.Button(login_frame, width=6, text="Sign up",font=("playfair",23), border=0, bg="#222222", cursor="hand2", fg="#57a1f8")
Signup_button.place(x=410, y=612)

# Add the About us button
about_button = tk.Button(login_frame, width=10, text=" About us ℹ️",font=("playfair",13), border=0, bg="#222222", cursor="hand2", fg="#57a1f8")
about_button.place(x=700, y=790)


root.protocol("WM_DELETE_WINDOW", on_closing)  # Attach close event handler
# Run the application loop
root.mainloop()