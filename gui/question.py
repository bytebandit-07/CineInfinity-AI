import tkinter as tk
import customtkinter as ctk

root=ctk.CTk()
root._set_appearance_mode("dark")
root.title("What do you like?")
root.geometry("600x700")
root.resizable(False,False)

heading=ctk.CTkLabel(root,text="Tell us your preferences")

root.mainloop()