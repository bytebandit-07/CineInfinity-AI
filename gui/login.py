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
root.geometry("1280x900")  # Set window size
root.configure(bg="#262626")  # Set background color



# Welcome text
welcome_text = "Film Flow ▶️"
welcome_label = ctk.CTkLabel(root, text="", font=("anton",50,"bold"),text_color="#fda600")
welcome_label.place(x=50,y=30)

#Welcome animation
def type_welcome(index=0):
    if index < len(welcome_text):
        welcome_label.configure(text=welcome_text[:index+1])
        root.after(100, lambda: type_welcome(index+1))

type_welcome()  # Start the typing animation

#adding frame as underline
under_frame1=ctk.CTkFrame(root, width=280, height=2, fg_color="#fda600").place(x=50,y=80)
under_frame2=ctk.CTkFrame(root, width=280, height=2, fg_color="#fda600").place(x=50,y=90)

# Outer frame (Border effect)
outer_frame = ctk.CTkFrame(root, 
                           width=550, height=570,  # Set width & height in constructor
                           corner_radius=10, 
                           fg_color="#fda600")  # Border color
outer_frame.place(x=690, y=75)  # Place without width/height


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
usr_label = tk.Label(login_frame, text="Username", font=("playfair", 23, 'bold'), bg="#222222", fg="#fda600")
usr_label.place(x=62, y=150)

pass_label = tk.Label(login_frame, text="Password", font=("playfair", 23, 'bold'), bg="#222222", fg="#fda600")
pass_label.place(x=67, y=270)

# Adding input fields for username and password
login_text = tk.Entry(login_frame, width=25, fg='white', border=0, bg="#222222", font=("arial", 23))
login_text.place(x=234, y=144)

password_text = tk.Entry(login_frame, width=25, fg='white', border=0, bg="#222222", font=("arial", 23), show="*")
password_text.place(x=230, y=270)

#adding frame as underline
under_frame3=ctk.CTkFrame(login_frame, width=284, height=2, fg_color="#fda600").place(x=157,y=123)
under_frame4=ctk.CTkFrame(login_frame, width=286, height=2, fg_color="#fda600").place(x=155,y=208)


# Bounce button animation
def bounce_button():
    original_y = 265
    for offset in [0, -5, -10, -5, 0]:
        Login_button.place(x=210, y=original_y + offset)
        root.update()
        root.after(30)

#Login button
Login_button = ctk.CTkButton(
    master=login_frame, text="LOGIN",fg_color="#fda600",hover_color='#0096ff', command=lambda: [bounce_button(), on_button_click()]
)
Login_button.place(x=210, y=265)
#Adding OR label
OR_label = tk.Label(login_frame, text="----------OR----------", font=("playfair", 26), bg="#222222", fg="white")
OR_label.place(x=255,y=510)

# Add a label for the sign-up option
Signup_label = tk.Label(login_frame, text="Don't have an account? ", bg="#222222", fg="white", font=("playfair", 23) )
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