from tkinter import *
import Pmw 

root = Tk()
Pmw.initialise(root)

# Create some random widget
button = Button(root, text = " This is a Test", pady = 30)
button.pack(pady = 10)

# create ballon object and bind it to the widget 
balloon = Pmw.Balloon(root)
balloon.bind(button,"Text for the tool tip")

mainloop()