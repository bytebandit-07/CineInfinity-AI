import customtkinter as ctk

root=ctk.CTk()
ctk.set_appearance_mode('dark')
root.geometry('1250x600')
root.title('about us')
root.resizable(False,False)


frame1=ctk.CTkFrame(root,fg_color='#333333',width=250,height=320,corner_radius=50).place(x=50,y=250)
frame1.

frame2=ctk.CTkFrame(root,fg_color='#333333',width=250,height=320,corner_radius=50).place(x=350,y=250)

frame3=ctk.CTkFrame(root,fg_color='#333333',width=250,height=320,corner_radius=50).place(x=650,y=250)

frame4=ctk.CTkFrame(root,fg_color='#333333',width=250,height=320,corner_radius=50).place(x=950,y=250)


root.mainloop()