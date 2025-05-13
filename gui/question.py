import tkinter as tk
import customtkinter as ctk


def on_checkbox_toggle():
    if select1.get() == 1:  # Checkbox is checked
        # Change text color to red
        select1.configure(text_color="red")

        # Shake animation
        shake_checkbox(5)


def shake_checkbox(count):
    """Recursive function to create shake effect"""
    x = -5 if count % 2 else 5
    select1.grid(padx=(20 + x, 0))  # Adjust only left padding

    if count > 0:
        root.after(50, shake_checkbox, count - 1)
    else:
        # Reset to original position after shaking
        select1.grid(padx=20)

root=ctk.CTk()
root._set_appearance_mode("dark")
root.title("What do you like?")
root.geometry("600x700")
root.resizable(False,False)
heading=ctk.CTkLabel(root,text="Tell us your preferences 🧐",text_color="white",font=('joyous',22,'bold'))
heading.grid(row=0,column=0,padx=180,pady=14)

select1=ctk.CTkCheckBox(root,text="Horror 💀",font=('Tempus Sans ITC',22,'bold'),command=on_checkbox_toggle)
select1.grid(row=1,column=0,padx=20,pady=0,sticky="w")




root.mainloop()