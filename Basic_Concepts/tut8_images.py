from tkinter import * 
from PIL import Image, ImageTk


root = Tk()
root.title("Images")

# btn = Button(root, text = "Exit", command=quit).pack()
# btn = Button(root, text = "Exit", command=root.quit).pack()

my_img = Image.open("img/1.jpg")
rez = my_img.resize((300, 200), Image.ANTIALIAS) 
img = ImageTk.PhotoImage(rez)
Label(image=img).pack()

root.mainloop() 