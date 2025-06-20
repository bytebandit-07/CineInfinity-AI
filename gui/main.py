import os
import customtkinter as ctk
from PIL import Image
from customtkinter import CTkImage
from backend.app import CineInfinityBackend
from gui.register import show_register_window
from gui.about import show_about_window
from gui.main_window import show_main

def show_login():
    backend = CineInfinityBackend()
    root = ctk.CTk()
    ctk.set_appearance_mode("dark")
    root.title("Film Flow - Login")
    root.geometry("1200x750")
    root.configure(bg="#0A0A0A")
    try:
        _SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
        _ASSETS_DIR = os.path.join(_SCRIPT_DIR, os.pardir, "Assets")
        ICON_PATH = os.path.join(_ASSETS_DIR, "labeel.ico")
        POSTER1 = os.path.join(_ASSETS_DIR, "poster1.jpg")
        POSTER2 = os.path.join(_ASSETS_DIR, "poster2.jpg")
        root.iconbitmap(ICON_PATH)
    except:
        pass

    # --- UI Layout ---
    bg_frame = ctk.CTkFrame(root, fg_color="#0A0A0A")
    bg_frame.pack(fill="both", expand=True)
    _SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
    _ASSETS_DIR = os.path.join(_SCRIPT_DIR, os.pardir, "Assets")
    ICON_PATH = os.path.join(_ASSETS_DIR, "labeel.ico")
    POSTER1 = os.path.join(_ASSETS_DIR, "poster1.jpg")
    POSTER2 = os.path.join(_ASSETS_DIR, "poster2.jpg")
    root.iconbitmap(ICON_PATH)
    poster_frame = ctk.CTkFrame(bg_frame, fg_color="transparent", width=500)
    poster_frame.pack(side="left", fill="y", padx=20)
    for path in (POSTER1, POSTER2):
        try:
            img = Image.open(path)
            ctk_img = CTkImage(light_image=img, size=(300,350))
            lbl = ctk.CTkLabel(poster_frame, image=ctk_img, text="")
            lbl.image = ctk_img
            lbl.pack(pady=15)
        except:
            placeholder = ctk.CTkFrame(poster_frame, width=300, height=450,
                                       corner_radius=12, fg_color="#1A1A1A")
            placeholder.pack(pady=15)

    login_container = ctk.CTkFrame(bg_frame, width=600, corner_radius=20,
                                   fg_color="#111111", border_width=1, border_color="#222222")
    login_container.pack(side="right", fill="both", expand=True, padx=40, pady=40)

    logo_frame = ctk.CTkFrame(login_container, fg_color="transparent")
    logo_frame.pack(pady=(50,30))
    ctk.CTkLabel(logo_frame, text="🎬 FILM FLOW", font=("Impact",42), text_color="#E50914").pack()
    ctk.CTkLabel(logo_frame, text="Your Personal Movie Recommender",
                 font=("Helvetica",16), text_color="#888888").pack(pady=(5,0))

    form_frame = ctk.CTkFrame(login_container, fg_color="transparent")
    form_frame.pack(pady=(0,20), padx=80, fill="x")
    ctk.CTkLabel(form_frame, text="USERNAME", font=("Helvetica",12,"bold"), text_color="#AAAAAA").pack(anchor="w")
    login_text = ctk.CTkEntry(form_frame, placeholder_text="Enter your username",
                              height=48, fg_color="#1A1A1A", corner_radius=8)
    login_text.pack(fill="x", pady=(5,10))
    ctk.CTkLabel(form_frame, text="PASSWORD", font=("Helvetica",12,"bold"), text_color="#AAAAAA").pack(anchor="w")
    pw_frame = ctk.CTkFrame(form_frame, fg_color="transparent")
    pw_frame.pack(fill="x", pady=(5,10))
    password_text = ctk.CTkEntry(pw_frame, placeholder_text="Enter your password",
                                 show="*", height=48, fg_color="#1A1A1A", corner_radius=8)
    password_text.pack(side="left", fill="x", expand=True)
    toggle_btn = ctk.CTkButton(pw_frame, text="👁️", width=30, height=28,
                               fg_color="transparent", hover_color="#222222",
                               command=lambda: password_text.configure(
                                   show='' if password_text.cget('show') == '*' else '*'))
    toggle_btn.pack(side="right", padx=(5,0))

    error_label = ctk.CTkLabel(form_frame, text="", font=("Helvetica",12), text_color="#FF5555")
    error_label.pack(pady=(0,10))

    login_btn = ctk.CTkButton(form_frame, text="START STREAMING",
                               fg_color="#E50914", hover_color="#C40812",
                               font=("Helvetica",16,"bold"), height=50,
                               corner_radius=8)
    login_btn.pack(pady=(10,30), fill="x")

    footer = ctk.CTkFrame(login_container, fg_color="transparent")
    footer.pack(fill="x", pady=(0,40), padx=80)
    ctk.CTkLabel(footer, text="New to Film Flow?", font=("Helvetica",13), text_color="#777777").pack(side="left")
    signup_btn = ctk.CTkButton(footer, text="Create Account",
                               fg_color="transparent", hover_color="#222222",
                               font=("Helvetica",13,"underline"), text_color="#57a1f8")
    signup_btn.pack(side="left", padx=5)
    about_btn = ctk.CTkButton(footer, text="About Us", fg_color="transparent",
                              hover_color="#222222", font=("Helvetica",13), text_color="#777777")
    about_btn.pack(side="right")

    # --- Bind callbacks ---
    def on_login():
        user = login_text.get().strip()
        pwd = password_text.get()
        if backend.login(user, pwd):
            root.destroy()
            show_main(backend, user)
        else:
            error_label.configure(text="Invalid credentials - Try again")
    login_btn.configure(command=on_login)
    signup_btn.configure(command=lambda: (root.withdraw(), show_register_window(root, backend)))
    about_btn.configure(command=lambda: (root.withdraw(), show_about_window(root)))

    root.protocol("WM_DELETE_WINDOW", root.destroy)
    root.mainloop()