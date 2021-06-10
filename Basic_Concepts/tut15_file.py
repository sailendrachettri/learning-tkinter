from tkinter import * 
from tkinter import filedialog
from PIL import Image, ImageTk

root = Tk()
root.title("File open Dialog Box")




def open_file():
    global img 
    filename = filedialog.askopenfilename(initialdir="/home/sailendrachettri/Pictures/Stock Images/", title="Select a file", filetypes=(('png files', '*.png'), ('jpg files', '*.jpg'),('all files', '*.*'))) 
    my_label = Label(root, text=filename).pack()
    my_image = Image.open(filename)
    resize = my_image.resize((300, 200), Image.ANTIALIAS)
    img = ImageTk.PhotoImage(resize) 
    my_image_label = Label(root, image=img)
    my_image_label.pack()

my_btn = Button(root, text="Open file", command= open_file).pack()

root.mainloop()  

