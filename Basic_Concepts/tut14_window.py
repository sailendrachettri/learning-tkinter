from tkinter import * 
from PIL import Image, ImageTk

root = Tk()
root.title("Main Window - Sailendra")

def open_second():
    global my_image
    global img 
    global resize
    top = Toplevel()
    top.title("Second Window - Sailendra")

    my_img =  Image.open('img/1.jpg')
    resize = my_img.resize((300, 200), Image.ANTIALIAS)
    img = ImageTk.PhotoImage(resize)
    Label(top, image=img).pack()
    btn2 = Button(top, text="Close window", command=top.destroy)
    btn2.pack()

btn = Button(root, text="Open Second window", command=open_second)
btn.pack()


root.mainloop()