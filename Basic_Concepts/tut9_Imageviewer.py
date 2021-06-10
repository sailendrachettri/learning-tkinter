from tkinter import * 
from PIL import ImageTk, Image

root = Tk()
root.title("Image Viewer")

my_img1 = Image.open("img/1.jpg")
rez1 = my_img1.resize((300, 300), Image.ANTIALIAS)
img1 = ImageTk.PhotoImage(rez1) 

my_img2 = Image.open("img/2.jpg")
rez2 = my_img2.resize((300, 300), Image.ANTIALIAS)
img2 = ImageTk.PhotoImage(rez2) 

my_img3 = Image.open("img/3.jpg")
rez3 = my_img3.resize((300, 300), Image.ANTIALIAS)
img3 = ImageTk.PhotoImage(rez3) 

my_img4 = Image.open("img/4.jpg")
rez4 = my_img4.resize((300, 300), Image.ANTIALIAS)
img4 = ImageTk.PhotoImage(rez4) 

my_img5 = Image.open("img/5.jpg")
rez5 = my_img5.resize((300, 300), Image.ANTIALIAS)
img5 = ImageTk.PhotoImage(rez5) 

image_list = [img1, img2, img3, img4, img5] 

status = Label(root, text="Image 1 of " + str(len(image_list)), bd=1, relief=SUNKEN, anchor=E)

my_label = Label(image=img1)
my_label.grid(row=0, column=0, columnspan=3)

def forward(image_number):
    global my_label
    global button_forward
    global button_back

    my_label.grid_forget() 
    my_label = Label(image=image_list[image_number-1])
    button_forward = Button(root, text=">>", command=lambda: forward(image_number+1))
    button_back = Button(root, text="<<", command=lambda: back(image_number-1))

    if image_number == 5:
        button_forward = Button(root, text=">>", state=DISABLED) 

    my_label.grid(row=0, column=0, columnspan=3)
    button_back.grid(row=1, column=0)
    button_forward.grid(row=1, column=2) 

    status = Label(root, text="Image "+ str(image_number) + " of " + str(len(image_list)), bd=1, relief=SUNKEN, anchor=E) 
    status.grid(row=2, column=0, columnspan=3, sticky=W+E)


def back(image_number):
    global my_label
    global button_forward
    global button_back

    my_label.grid_forget() 
    my_label = Label(image=image_list[image_number-1])
    button_forward = Button(root, text=">>", command=lambda: forward(image_number-1))
    button_back = Button(root, text="<<", command=lambda: back(image_number-1))

    if image_number == 1:
        button_back = Button(root, text="<<", state=DISABLED)


    my_label.grid(row=0, column=0, columnspan=3)
    button_back.grid(row=1, column=0)
    button_forward.grid(row=1, column=2) 

    #Update Status bar
    status = Label(root, text="Image "+ str(image_number) + " of " + str(len(image_list)), bd=1, relief=SUNKEN, anchor=E) 
    status.grid(row=2, column=0, columnspan=3, sticky=W+E)


button_back = Button(root, text="<<", command=back)
button_exit = Button(root, text="Exit", command=quit)
button_forward = Button(root, text=">>", command= lambda: forward(2))

button_back.grid(row=1, column=0)
button_exit.grid(row=1, column=1)
button_forward.grid(row=1, column=2, pady=10)
status.grid(row=2, column=0, columnspan=3, sticky=W+E)

root.mainloop()