from tkinter import * 
from tkinter import colorchooser

root = Tk()
root.title('Tkinter GUI - Sailendra')
root.geometry('400x400')

def color():
    my_color = colorchooser.askcolor()[1]
    my_label = Label(root, text=my_color).pack(pady=10)
    my_label_2 = Label(root, text="This is the color you choosed", font="Helvetica 20", bg=my_color).pack()

my_button = Button(root, text="Choose", command=color).pack()


root.mainloop()