from os import getenvb
from tkinter import * 

root = Tk()
root.title('Tkinter GUI - Sailendra')
root.geometry('400x500')

def clear():
    my_text.delete(1.0, END)

def get_text():
    my_label.config(text=my_text.get(1.0, END))  #1.0 to 3.0

my_text = Text(root, width=60, height=20)
my_text.pack(pady=20)

button_frame = Frame(root)
button_frame.pack()

clear_button = Button(button_frame, text="Clear Screen", command=clear)
clear_button.grid(row=0, column=0) 

get_text_button = Button(button_frame, text="Get text", command=get_text)
get_text_button.grid(row=0, column=1)

my_label = Label(root, text='')
my_label.pack(pady=20)

root.mainloop()