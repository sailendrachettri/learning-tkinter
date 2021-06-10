from tkinter import *

root = Tk() 

def myClick():
    Label(root, text="I create button!").pack()

# myButton = Button(root, text="Click Me!", state=DISABLED)
myButton = Button(root, command=myClick, text="Click Me!", padx=50, pady=50, fg="white", bg="#000000") 
myButton.pack()

root.mainloop() 