from tkinter import * 
from tut129_module1 import nameit

root = Tk()
root.title('Tkinter GUI - Sailendra')
root.geometry('400x400')

def submit():
    greet = nameit(my_box.get()) 
    my_label.config(text=greet)

my_box = Entry(root)
my_box.pack(pady=20) 

my_label = Label(root, text='', font=("Times New Roman", 30))
my_label.pack(pady=20)

my_button = Button(root, text="Submit Name", command=submit)
my_button.pack(pady=20) 

root.mainloop()