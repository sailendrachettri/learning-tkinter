from tkinter import * 
from PIL import Image
from PIL import ImageTk
from PIL.ImageTk import PhotoImage

root = Tk()
root.title('Tkinter GUI - Sailendra')
root.geometry('400x400')

my_pic = Image.open("img/1.jpg")

resized = my_pic.resize((300, 300), Image.ANTIALIAS)

new_pic = PhotoImage(resized)

my_label = Label(root, image=new_pic)
my_label.pack(pady=20)


root.mainloop()