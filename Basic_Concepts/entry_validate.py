# Import the required library
from tkinter import *
# Create an instance of tkinter frame or window
win = Tk()


def callback(input):
    if input.isdigit():
        print(input)
        return True
    elif input == "":
        print(input)
        return True
    else:
        print(input)
        return False


# Create an entry widget
entry = Entry(win)
fun = win.register(callback)
entry.config(validate="key", validatecommand=(fun, '%P'))
entry.pack()
win.mainloop()
