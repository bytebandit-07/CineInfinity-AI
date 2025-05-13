import tkinter as tk
import customtkinter as ctk


def on_checkbox_toggle(checkbox):
    """Handle checkbox toggle with animation and color change"""
    if checkbox == select1:
        color = "red"  # Horror color
    elif checkbox == select2:
        color = "#FF69B4"  # Romance color (hot pink)
    elif checkbox== select3:
        color = "#FFD300"
    elif checkbox== select4:
        color = "#f7ee6d"

    if checkbox.get() == 1:  # Checkbox is checked
        checkbox.configure(text_color=color)
        shake_checkbox(checkbox, 5)
    else:  # Checkbox is unchecked
        checkbox.configure(text_color=ctk.ThemeManager.theme["CTkCheckBox"]["text_color"])


def shake_checkbox(checkbox, count):
    """Recursive function to create shake effect"""
    x = -5 if count % 2 else 5
    if checkbox == select1:
        checkbox.grid(padx=(20 + x, 0))
    elif checkbox == select2:
        checkbox.grid(padx=(20 + x, 0))
    elif checkbox == select3:
        checkbox.grid(padx=(20 + x, 0))
    elif checkbox == select4:
        checkbox.grid(padx=(20 + x, 0))


    if count > 0:
        root.after(50, shake_checkbox, checkbox, count - 1)
    else:
        # Reset to original position after shaking
        if checkbox == select1:
            checkbox.grid(padx=20)
        elif checkbox == select2:
            checkbox.grid(padx=20)
        elif checkbox == select3:
            checkbox.grid(padx=20)
        elif checkbox == select4:
            checkbox.grid(padx=20)


root=ctk.CTk()
root._set_appearance_mode("dark")
root.title("What do you like?")
root.geometry("600x700")
root.resizable(False,False)
heading=ctk.CTkLabel(root,text="Tell us your preferences 🧐",text_color="white",font=('joyous',32,'bold'))
heading.grid(row=0,column=0,padx=88,pady=14)

select1=ctk.CTkCheckBox(root,text="Horror 💀",font=('Tempus Sans ITC',22,'bold'),command=lambda:on_checkbox_toggle(select1))
select1.grid(row=1,column=0,padx=20,pady=0,sticky="w")

select2=ctk.CTkCheckBox(root,text="Romance 💘",font=('Calisto MT',22,'bold'),command=lambda:on_checkbox_toggle(select2))
select2.grid(row=2,column=0,padx=20,pady=12,sticky="w")

select3=ctk.CTkCheckBox(root,text="Action 🚁",font=('Arial Rounded MT Bold',22),command=lambda:on_checkbox_toggle(select3))
select3.grid(row=3,column=0,padx=20,pady=12,sticky="w")

select4=ctk.CTkCheckBox(root,text="Comedy 🎭",font=('Book Antiqua Bold',22,'bold'),command=lambda:on_checkbox_toggle(select4))
select4.grid(row=4,column=0,padx=20,pady=12,sticky="w")

root.mainloop()