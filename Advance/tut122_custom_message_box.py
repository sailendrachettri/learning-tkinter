from tkinter import * 
from PIL import Image
from PIL.ImageTk import PhotoImage

root = Tk()
root.title('Tkinter GUI - Sailendra')
root.geometry('400x400')

def choice(option):
    pop.destroy()
    if option == "yes":
        my_label.config(text="You clicked yes.")
    else:
        my_label.config(text="You clicked no.")

def clicker():
    global pop
    pop = Toplevel(root)
    pop.title("My popup") 
    pop.geometry("250x150")
    pop.config(bg="pink")

    global me
    me = Image.open("img/digital_clock.png")
    resize = me.resize((30, 30), Image.ANTIALIAS)
    me = PhotoImage(resize) 

    pop_label = Label(pop, text="Would you like to proceed?", bg="pink", fg="#EEEEEE")
    pop_label.pack(pady=10)

    my_frame = Frame(pop, bg="pink")
    my_frame.pack(pady=5)

    me_pic = Label(my_frame, image=me, borderwidth=0)
    me_pic.grid(row=0, column=0, padx=10) 

    yes = Button(my_frame, text="Yes", command=lambda: choice("yes"), bg="orange")
    yes.grid(row=0, column=1, padx=10)

    no = Button(my_frame, text="No", command=lambda: choice("no"), bg="yellow")
    no.grid(row=0, column=2, padx=10)

my_button = Button(root, text="Click me!", command=clicker)
my_button.pack(pady=20) 

my_label = Label(root, text="")
my_label.pack(pady=10) 
root.mainloop()