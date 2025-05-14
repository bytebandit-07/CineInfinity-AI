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
heading.grid(row=0,column=0,padx=88,pady=14,sticky="W")

select1=ctk.CTkCheckBox(root,text="Horror 💀",font=('Tempus Sans ITC',22,'bold'),command=lambda:on_checkbox_toggle(select1))
select1.grid(row=1,column=0,padx=20,pady=0,sticky="w")

select2=ctk.CTkCheckBox(root,text="Romance 💘",font=('Calisto MT',22,'bold'),command=lambda:on_checkbox_toggle(select2))
select2.grid(row=2,column=0,padx=20,pady=12,sticky="w")

select3=ctk.CTkCheckBox(root,text="Action 🚁",font=('Arial Rounded MT Bold',22),command=lambda:on_checkbox_toggle(select3))
select3.grid(row=3,column=0,padx=20,pady=12,sticky="w")

select4=ctk.CTkCheckBox(root,text="Comedy 🎭",font=('Book Antiqua Bold',22,'bold'),command=lambda:on_checkbox_toggle(select4))
select4.grid(row=4,column=0,padx=20,pady=12,sticky="w")

select5=ctk.CTkCheckBox(root,text="Adventure 🗺️",font=('Book Antiqua Bold',22,'bold'),command=lambda:on_checkbox_toggle(select4))
select5.grid(row=5,column=0,padx=20,pady=12,sticky="w")

select6=ctk.CTkCheckBox(root,text="Animation 🎨",font=('Book Antiqua Bold',22,'bold'),command=lambda:on_checkbox_toggle(select4))
select6.grid(row=6,column=0,padx=20,pady=12,sticky="w")

select7=ctk.CTkCheckBox(root,text="Children 🧒",font=('Book Antiqua Bold',22,'bold'),command=lambda:on_checkbox_toggle(select4))
select7.grid(row=7,column=0,padx=20,pady=12,sticky="w")

select8=ctk.CTkCheckBox(root,text="Crime 🕵️",font=('Book Antiqua Bold',22,'bold'),command=lambda:on_checkbox_toggle(select4))
select8.grid(row=8,column=0,padx=20,pady=12,sticky="w")

select9=ctk.CTkCheckBox(root,text="Documentary 📚",font=('Book Antiqua Bold',22,'bold'),command=lambda:on_checkbox_toggle(select4))
select9.grid(row=9,column=0,padx=20,pady=12,sticky="w")

select10=ctk.CTkCheckBox(root,text="Drama 🎬",font=('Book Antiqua Bold',22,'bold'),command=lambda:on_checkbox_toggle(select4))
select10.grid(row=10,column=0,padx=20,pady=12,sticky="w")

select10=ctk.CTkCheckBox(root,text="Fantasy 🧚",font=('Book Antiqua Bold',22,'bold'),command=lambda:on_checkbox_toggle(select4))
select10.grid(row=1,column=0,padx=350,pady=12,sticky ="W")

select11=ctk.CTkCheckBox(root,text="Film-Noir 🌑",font=('Book Antiqua Bold',22,'bold'),command=lambda:on_checkbox_toggle(select4))
select11.grid(row=2,column=0,padx=350,pady=12,sticky ="W")

select12=ctk.CTkCheckBox(root,text="IMAX 🎥",font=('Book Antiqua Bold',22,'bold'),command=lambda:on_checkbox_toggle(select4))
select12.grid(row=3,column=0,padx=350,pady=12,sticky ="W")

select13=ctk.CTkCheckBox(root,text="Musical 🎵",font=('Book Antiqua Bold',22,'bold'),command=lambda:on_checkbox_toggle(select4))
select13.grid(row=4,column=0,padx=350,pady=12,sticky ="W")

select14=ctk.CTkCheckBox(root,text="Mystery 🕵️‍♂️",font=('Book Antiqua Bold',22,'bold'),command=lambda:on_checkbox_toggle(select4))
select14.grid(row=5,column=0,padx=350,pady=12,sticky ="W")

select15=ctk.CTkCheckBox(root,text="Sci-Fi 👽",font=('Book Antiqua Bold',22,'bold'),command=lambda:on_checkbox_toggle(select4))
select15.grid(row=6,column=0,padx=350,pady=12,sticky ="W")

select16=ctk.CTkCheckBox(root,text="Thriller 😱",font=('Book Antiqua Bold',22,'bold'),command=lambda:on_checkbox_toggle(select4))
select16.grid(row=7,column=0,padx=350,pady=12,sticky ="W")

select17=ctk.CTkCheckBox(root,text="War ⚔️",font=('Book Antiqua Bold',22,'bold'),command=lambda:on_checkbox_toggle(select4))
select17.grid(row=8,column=0,padx=350,pady=12,sticky ="W")

select18=ctk.CTkCheckBox(root,text="Western 🤠",font=('Book Antiqua Bold',22,'bold'),command=lambda:on_checkbox_toggle(select4))
select18.grid(row=9,column=0,padx=350,pady=12,sticky ="W")


root.mainloop()