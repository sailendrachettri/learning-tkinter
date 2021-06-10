from tkinter import * 
from tkinter import ttk
root = Tk()
root.title("Adding Frame")

frame = LabelFrame(root, text= "This is my Frame...", padx=50, pady=50)
frame.pack(padx=100, pady=100)

b = Button(frame, text="Don't click here")
b2 = Button(frame, text="Don't click 2")

b.grid(row=0, column=0)
b2.grid(row=1, column=0)

root.mainloop()  