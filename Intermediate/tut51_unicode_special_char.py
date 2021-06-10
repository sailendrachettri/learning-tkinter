from tkinter import *
from tkinter import font
from tkinter.font import Font 

root = Tk()
root.title('Tkinter GUI - Sailendra')
root.geometry('400x400')

my_label = Label(root, text='41'+ u'\u00b0', font="Helvetica 30").pack(pady=10)
my_button = Button(root, text=u'\u00BB', font="Helvetica 20").pack(pady=10)
# print('100' + u'\u00b0')
root.mainloop()