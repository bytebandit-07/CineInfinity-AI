import customtkinter as ctk
import webbrowser
from PIL import Image
import tkinter as tk


def show_about_window(parent):
    def open_link(url):
        webbrowser.open_new(url)

    def on_closing():
        about_window.destroy()
        parent.deiconify()  # Show login window again

    about_window = ctk.CTkToplevel()
    about_window.title("about us")
    about_window.iconbitmap("../Assets/labeel.ico")
    about_window.geometry('1250x600')

    about_window.resizable(False, False)
    ctk.set_appearance_mode('dark')
    about_window.protocol("WM_DELETE_WINDOW", on_closing)


    # === Developer content (USE YOUR EXISTING CODE BELOW THIS LINE) ===
    container = ctk.CTkFrame(about_window, fg_color="transparent")
    container.grid(row=1, column=0, pady=90)

    frame1 = ctk.CTkFrame(container, fg_color='#333333', width=250, height=370, corner_radius=50)
    frame1.grid(row=0, column=0, padx=50)
    frame1.pack_propagate(False)

    frame2 = ctk.CTkFrame(container, fg_color='#333333', width=250, height=370, corner_radius=50)
    frame2.grid(row=0, column=1, padx=20)
    frame2.pack_propagate(False)

    frame3 = ctk.CTkFrame(container, fg_color='#333333', width=250, height=370, corner_radius=50)
    frame3.grid(row=0, column=2, padx=20)
    frame3.pack_propagate(False)

    frame4 = ctk.CTkFrame(container, fg_color='#333333', width=250, height=370, corner_radius=50)
    frame4.grid(row=0, column=3, padx=20)
    frame4.pack_propagate(False)

    image1 = ctk.CTkImage(Image.open(r'../Assets/Omi.jpg'), size=(250, 250))
    image1_label = ctk.CTkLabel(frame1, image=image1, text="", corner_radius=100)
    image1_label.pack(pady=30)

    link1 = ctk.CTkLabel(frame1, text="M Umar Nasir", text_color="white", font=('Arial', 18, 'bold'), cursor="hand2")
    link1.pack(pady=(10, 0))
    link1.bind("<Button-1>", lambda e: open_link("https://github.com/omidrogado"))

    image2 = ctk.CTkImage(Image.open(r'../Assets/Talha.jpg'), size=(250, 250))
    image2_label = ctk.CTkLabel(frame2, image=image2, text="", corner_radius=100)
    image2_label.pack(pady=30)

    link2 = ctk.CTkLabel(frame2, text="M talha Aamir", text_color="white", font=('Arial', 18, 'bold'), cursor="hand2")
    link2.pack(pady=(10, 0))
    link2.bind("<Button-1>", lambda e: open_link("https://github.com/NotTonyStarkk-99"))

    image3 = ctk.CTkImage(Image.open(r'../Assets/Talal.jpg'), size=(250, 250))
    image3_label = ctk.CTkLabel(frame3, image=image3, text="", corner_radius=100)
    image3_label.pack(pady=30)

    link3 = ctk.CTkLabel(frame3, text="M Talal", text_color="white", font=('Arial', 18, 'bold'), cursor="hand2")
    link3.pack(pady=(10, 0))
    link3.bind("<Button-1>", lambda e: open_link("https://github.com/bytebandit-07"))

    image4 = ctk.CTkImage(Image.open(r'../Assets/Ashir.jpg'), size=(250, 250))
    image4_label = ctk.CTkLabel(frame4, image=image4, text="", corner_radius=100)
    image4_label.pack(pady=30)

    link4 = ctk.CTkLabel(frame4, text="Ashir Bin Hamid", text_color="white", font=('Arial', 18, 'bold'), cursor="hand2")
    link4.pack(pady=(10, 0))
    link4.bind("<Button-1>", lambda e: open_link("https://github.com/Lordshadow-afk"))

    frame_label = ctk.CTkLabel(about_window, text="DEVELOPERS", text_color='white', font=('Terminal', 45, 'bold'))
    frame_label.grid(row=0, column=0, padx=195, pady=40)





