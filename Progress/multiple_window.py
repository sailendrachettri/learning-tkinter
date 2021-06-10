#how to create multiple windows in tkinter with button
from tkinter import * 

root = Tk()
root.title('Tkinter GUI - Sailendra')
root.geometry('400x400')

# This function is able to create new seperated window
def new_window():
    new_root = Tk()
    new_root.title("New Tkinter Window")
    new_root.geometry("500x500") 

#Button to create new window when it clicked 
my_button = Button(root, text="Create New Window", command=new_window) 
my_button.pack()

root.mainloop()