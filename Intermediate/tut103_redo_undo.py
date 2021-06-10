from os import getenvb, name, remove
from tkinter import * 
from tkinter import filedialog
from PIL.ImageTk import PhotoImage
from PIL import Image
from tkinter import font

# 102: bold, italics

root = Tk()
root.geometry('400x700')

def open_txt():
    text_file = filedialog.askopenfilename(initialdir="/home/sailendrachettri/Learning /codes/Tkinter_CODEMY/", title="Open Text File", filetypes=(("Text Files", "*.txt"), ))
    name = text_file
    text_file = open(text_file, "r")
    stuff = text_file.read() 

    my_text.insert(END, stuff)
    text_file.close() 

    # Set title 
    root.title(f"{name} - Textpad")

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

def select():
    selected = my_text.selection_get()
    my_label.config(text=selected)

def bolder():
    bold_font = font.Font(my_text, my_text.cget("font")) 
    bold_font.configure(weight="bold") 

    my_text.tag_configure("bold", font=bold_font) 

    current_tags = my_text.tag_names("sel.first") 

    if "bold" in current_tags:
        my_text.tag_remove("bold", "sel.first", "sel.last")
    else:
        my_text.tag_add("bold", "sel.first", "sel.last") 
        

def italics_it():
    italics_font = font.Font(my_text, my_text.cget("font"))
    italics_font.configure(slant="italic")

    my_text.tag_configure("italic", font=italics_font)

    current_tags = my_text.tag_names("sel.first") 

    if "italic" in current_tags:
        my_text.tag_remove("italic", "sel.first", "sel.last")
    else:
        my_text.tag_add("italic", "sel.first", "sel.last") 
        
    

my_frame = Frame(root)
my_frame.pack(pady=10) 

#Create scroll bar
text_scrollbar = Scrollbar(my_frame)
text_scrollbar.pack(side=RIGHT, fill=Y)

my_text = Text(my_frame, width=40, height=10, font="Courier 14", selectbackground="blue", selectforeground="white", yscrollcommand=text_scrollbar.set, undo=True)
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

# Select button
select_button = Button(root, text="Select Text", command=select)
select_button.pack(pady=5)

#Bold button
bold_button = Button(root, text="Bold", command=bolder)
bold_button.pack(pady=5)

#italics buttons
italics_button = Button(root, text="Italics", command=italics_it)
italics_button.pack(pady=5)

#Undo button
undo_button = Button(root, text="undo", command=my_text.edit_undo)
undo_button.pack(pady=5) 

#Redo button
redo_button = Button(root, text="redo", command=my_text.edit_redo)
redo_button.pack(pady=5) 



my_label = Label(root, text="")
my_label.pack()



root.mainloop()