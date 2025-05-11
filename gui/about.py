import customtkinter as ctk
import random
from itertools import cycle

root = ctk.CTk()
ctk.set_appearance_mode('dark')
root.geometry('1250x600')
root.title('about us')
root.resizable(False, False)

# Create the label
frame_label = ctk.CTkLabel(root, text="DEVELOPERS", text_color='white', font=('Terminal', 35, 'bold'))
frame_label.place(x=515, y=100)

# Glitch colors
glitch_colors = ['#ff00ff', '#00ffff', '#ffff00', '#ff0000', '#00ff00', '#0000ff']
color_cycle = cycle(glitch_colors)

# Shaking animation parameters
SHAKE_INTENSITY = 15  # Maximum shake distance in pixels
SHAKE_STEPS = 5  # Number of shake movements per glitch


def shake_label():
    """Perform the shaking animation"""
    for i in range(SHAKE_STEPS):
        # Calculate progressive shake (stronger at first, then weaker)
        intensity = SHAKE_INTENSITY * (SHAKE_STEPS - i) / SHAKE_STEPS

        # Random offset that decreases over time
        x_offset = 515 + random.randint(-int(intensity), int(intensity))
        y_offset = 100 + random.randint(-int(intensity / 2), int(intensity / 2))

        # Schedule each shake step with increasing delay for damping effect
        root.after(i * 30, lambda x=x_offset, y=y_offset: frame_label.place(x=x, y=y))

    # Final reset to original position
    root.after(SHAKE_STEPS * 30, lambda: frame_label.place(x=515, y=100))


def glitch_animation():
    # Randomly change some characters
    original_text = "DEVELOPERS"
    glitched_text = list(original_text)

    # Change 1-3 random characters to symbols
    for _ in range(random.randint(1, 3)):
        idx = random.randint(0, len(glitched_text) - 1)
        glitched_text[idx] = random.choice(['@', '#', '$', '%', '&', '*', '?'])

    # Join the text back together
    glitched_text = ''.join(glitched_text)

    # Apply changes
    frame_label.configure(text=glitched_text, text_color='#0ffbf9')

    # Start shaking animation
    shake_label()

    # Schedule the reset
    delay = random.randint(150, 400)  # Glitch duration
    root.after(delay, reset_glitch)


def reset_glitch():
    # Reset to original state
    frame_label.configure(text="DEVELOPERS", text_color='white')

    # Schedule next glitch
    delay = random.randint(800, 2000)  # Wait before next glitch
    root.after(delay, glitch_animation)


# Initial placement
frame_label.place(x=515, y=100)

# Start animation after 1 second
root.after(1000, glitch_animation)

# Background frames
frame1 = ctk.CTkFrame(root, fg_color='#333333', width=250, height=320, corner_radius=50).place(x=50, y=250)
frame2 = ctk.CTkFrame(root, fg_color='#333333', width=250, height=320, corner_radius=50).place(x=350, y=250)
frame3 = ctk.CTkFrame(root, fg_color='#333333', width=250, height=320, corner_radius=50).place(x=650, y=250)
frame4 = ctk.CTkFrame(root, fg_color='#333333', width=250, height=320, corner_radius=50).place(x=950, y=250)

root.mainloop()