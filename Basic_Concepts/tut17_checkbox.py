from tkinter import * 

root = Tk()
root.title('Tkinter GUI - Sailendra')
root.geometry('400x400')

var = StringVar()
var.set("Off")

c = Checkbutton(root, text="Check this box, I dare you!", variable=var, onvalue="On", offvalue="Off")
# c.deselect()
c.pack()


def show_value():
    my_Label = Label(root, text=var.get())
    my_Label.pack()

myButton = Button(root, text="Show value", command=show_value)
myButton.pack()


root.mainloop()