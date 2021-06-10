from os import getenvb
from tkinter import * 
from tkinter import filedialog
from PIL.ImageTk import PhotoImage
from PIL import Image

root = Tk()
root.title('Tkinter GUI - Sailendra')
root.geometry('400x500')

def open_txt():
    text_file = filedialog.askopenfilename(initialdir="/home/sailendrachettri/Learning /codes/Tkinter_CODEMY/", title="Open Text File", filetypes=(("Text Files", "*.txt"), ))
    text_file = open(text_file, "r")

    stuff = text_file.read() 
    my_text.insert(END, stuff)
    text_file.close() 

def save_txt():
    text_file = open("/home/sailendrachettri/Learning /codes/Tkinter_CODEMY/Samples/tut100_.txt", 'w')
    text_file.write(my_text.get(1.0, END)) 

def add_image():
    image = Image.open("img/4.jpg")
    resized = image.resize((100, 100), Image.ANTIALIAS)

    global new_image
    new_image = PhotoImage(resized)
    position = my_text.index(INSERT)
    my_text.image_create(position, image=new_image)

    my_label.config(text=position)

my_frame = Frame(root)
my_frame.pack(pady=10) 

#Create scroll bar
text_scrollbar = Scrollbar(my_frame)
text_scrollbar.pack(side=RIGHT, fill=Y)

my_text = Text(my_frame, width=40, height=10, font="Courier 14", selectbackground="blue", selectforeground="white", yscrollcommand=text_scrollbar.set)
my_text.pack(pady=10)

# Configure scrollbar
text_scrollbar.config(command=my_text.yview)


open_button = Button(root, text="Open Text File", command=open_txt)
open_button.pack(pady=10) 

save_button = Button(root, text="Save File", command=save_txt)
save_button.pack(pady=10) 


#image label
image_button = Button(root, text="Add Image", command=add_image)
image_button.pack(pady=4)


my_label = Label(root, text="")
my_label.pack()

root.mainloop()