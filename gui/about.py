import customtkinter as ctk
import random
import webbrowser
from itertools import cycle
from PIL import Image
from PIL.ImageOps import expand


def open_link(url):
    webbrowser.open_new(url)

root = ctk.CTk()
ctk.set_appearance_mode('dark')
root.geometry('1250x600')
root.title('about us')
root.resizable(False, False)


# === Container for developer frames ===
container = ctk.CTkFrame(root, fg_color="transparent")
container.grid(row=1, column=0, pady=90)

# === Developer frames inside container ===
frame1 = ctk.CTkFrame(container, fg_color='#333333', width=250, height=370, corner_radius=50)
frame1.grid(row=0, column=0, padx=20,pady=100)
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

image1 = ctk.CTkImage(Image.open(r'E:\coding image\Omi.jpg'), size=(250, 250))
image1_label = ctk.CTkLabel(frame1, image=image1, text="", corner_radius=100)
image1_label.pack(pady=30)

link1 = ctk.CTkLabel(frame1, text="M Umar Nasir", text_color="white", font=('Arial', 18, 'bold'), cursor="hand2")
link1.pack(pady=(10, 0))
link1.bind("<Button-1>", lambda e: open_link("https://github.com/omidrogado"))

image2 = ctk.CTkImage(Image.open(r'E:\coding image\Talha.jpg'), size=(250, 250))
image2_label = ctk.CTkLabel(frame2, image=image2, text="", corner_radius=100)
image2_label.pack(pady=30)


link2 = ctk.CTkLabel(frame2, text="M talha Aamir", text_color="white", font=('Arial', 18, 'bold'), cursor="hand2")
link2.pack(pady=(10, 0))
link2.bind("<Button-1>", lambda e: open_link("https://github.com/NotTonyStarkk-99"))

image3 = ctk.CTkImage(Image.open(r'E:\coding image\Talal.jpg'), size=(250, 250))
image3_label = ctk.CTkLabel(frame3, image=image3, text="", corner_radius=100)
image3_label.pack(pady=30)

link3 = ctk.CTkLabel(frame3, text="M Talal", text_color="white", font=('Arial', 18, 'bold'), cursor="hand2")
link3.pack(pady=(10, 0))
link3.bind("<Button-1>", lambda e: open_link("https://github.com/bytebandit-07"))

image4 = ctk.CTkImage(Image.open(r'E:\coding image\Ashir.jpg'), size=(250, 250))
image4_label = ctk.CTkLabel(frame4, image=image4, text="", corner_radius=100)
image4_label.pack(pady=30)

link4 = ctk.CTkLabel(frame4, text="Ashir Bin Hamid", text_color="white", font=('Arial', 18, 'bold'), cursor="hand2")
link4.pack(pady=(10, 0))
link4.bind("<Button-1>", lambda e: open_link("https://github.com/Lordshadow-afk"))

# Create the label
frame_label = ctk.CTkLabel(root, text="DEVELOPERS", text_color='white', font=('Terminal', 35, 'bold'))
frame_label.place(x=515, y=100)

# Glitch colors
glitch_colors = ['#ff00ff', '#00ffff', '#ffff00', '#ff0000', '#00ff00', '#0000ff']
color_cycle = cycle(glitch_colors)

# Shaking animation parameters
SHAKE_INTENSITY = 15
SHAKE_STEPS = 5

def shake_label():
    for i in range(SHAKE_STEPS):
        intensity = SHAKE_INTENSITY * (SHAKE_STEPS - i) / SHAKE_STEPS
        x_offset = 515 + random.randint(-int(intensity), int(intensity))
        y_offset = 100 + random.randint(-int(intensity / 2), int(intensity / 2))
        root.after(i * 30, lambda x=x_offset, y=y_offset: frame_label.place(x=x, y=y))
    root.after(SHAKE_STEPS * 30, lambda: frame_label.place(x=515, y=100))

def glitch_animation():
    original_text = "DEVELOPERS"
    glitched_text = list(original_text)
    for _ in range(random.randint(1, 3)):
        idx = random.randint(0, len(glitched_text) - 1)
        glitched_text[idx] = random.choice(['@', '#', '$', '%', '&', '*', '?'])
    glitched_text = ''.join(glitched_text)
    frame_label.configure(text=glitched_text, text_color='#0ffbf9')
    shake_label()
    root.after(random.randint(150, 400), reset_glitch)

def reset_glitch():
    frame_label.configure(text="DEVELOPERS", text_color='white')
    root.after(random.randint(800, 2000), glitch_animation)

root.after(1000, glitch_animation)


root.mainloop()
