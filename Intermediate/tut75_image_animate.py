from tkinter import * 
from PIL import Image
from PIL.ImageTk import PhotoImage


root = Tk()
root.title('Tkinter GUI - Sailendra')
root.geometry('400x400')

def change(event):
    image = Image.open("img/2.jpg")
    resize = image.resize((400, 400), Image.ANTIALIAS)
    my_pic = PhotoImage(resize) 

    my_label.config(image=my_pic)
    my_label.image = my_pic

def change_back(event):
    image = Image.open("img/1.jpg")
    resize = image.resize((400, 400), Image.ANTIALIAS)
    my_pic = PhotoImage(resize) 

    my_label.config(image=my_pic)
    my_label.image = my_pic

def do_something():
    label2 = Label(root, text="You clicked the buton!!") 
    label2.pack() 
    
image = Image.open("img/1.jpg")
resize = image.resize((400, 400), Image.ANTIALIAS)
image = PhotoImage(resize)


my_label = Button(root, image=image, command=do_something)
my_label.pack(pady=10)

my_label.bind("<Enter>", change)
my_label.bind("<Leave>", change_back)


root.mainloop()