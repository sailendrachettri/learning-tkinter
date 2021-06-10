from os import getenvb
from tkinter import * 
from tkinter import filedialog

root = Tk()
root.title('Tkinter GUI - Sailendra')
root.geometry('400x500')

def open_txt():
    text_file = filedialog.askopenfilename(initialdir="/home/sailendrachettri/Learning /codes/Tkinter_CODEMY/", title="Open Text File", filetypes=(("Text Files", "*.txt"), ))
    text_file = open(text_file, "r")

    stuff = text_file.read() 
    my_text.insert(END, stuff)
    text_file.close() 

def save_txt():
    text_file = open("/home/sailendrachettri/Learning /codes/Tkinter_CODEMY/Samples/tut100_.txt", 'w')
    text_file.write(my_text.get(1.0, END)) 

my_text = Text(root, width=40, height=10, font="Courier 14")
my_text.pack(pady=10)

open_button = Button(root, text="Open Text File", command=open_txt)
open_button.pack(pady=10) 

save_button = Button(root, text="Save File", command=save_txt)
save_button.pack(pady=10) 

root.mainloop()