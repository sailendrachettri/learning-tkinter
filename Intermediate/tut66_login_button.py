from tkinter import * 
from PIL import Image
from PIL.ImageTk import PhotoImage

root = Tk()
root.title('Tkinter GUI - Sailendra')
root.geometry('400x400')

def btn_func():
    my_label.config(text="Clicked button")

login_button = Image.open('img/button.png')
resize_image = login_button.resize((200, 100), Image.ANTIALIAS)
img = PhotoImage(image=resize_image)

# image_label = Label(image=img) 
# image_label.pack(pady=20)

my_button = Button(root, image=img, command=btn_func, borderwidth=0, bg='blue')
my_button.pack(pady=20)

my_label = Label(root, text='')
my_label.pack(pady=20)

root.mainloop()