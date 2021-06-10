from tkinter import * 

root = Tk()
root.title('Tkinter GUI - Sailendra')
root.geometry('400x400')

def resize():
    w = width_entry.get()
    h = height_entry.get()
    root.geometry(f"{w}x{h}")  #Recommended
    # root.geometry("{width}x{height}".format(width=500, height=500)) 
    # root.geometry("%ix%i" % (w, h)) 

width_label = Label(root, text="Width: ")
width_label.pack(pady=20)

width_entry = Entry(root)
width_entry.pack(pady=20)

height_label = Label(root, text="Height: ")
height_label.pack(pady=20)

height_entry = Entry(root)
height_entry.pack(pady=20)


my_button = Button(root, text="Resize", command=resize)
my_button.pack(pady=20)


root.mainloop()