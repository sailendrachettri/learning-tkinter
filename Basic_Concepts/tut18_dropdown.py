from tkinter import * 
from tkinter import messagebox

root = Tk()
root.title('Tkinter GUI - Sailendra')
root.geometry('400x400')

def show():
    Label(root, text=clicked.get()).pack()

options = [
    "Monday",
    "Tuesday",
    "Wednesday",
    "Thusday",
    "Friday",
    "Saturday",
    "Sunday"
]

clicked = StringVar()
clicked.set("Select Option")
drop = OptionMenu(root, clicked, *options)
drop.pack()

myButton = Button(root, text="Show Selection", command=show)
myButton.pack()

root.mainloop()