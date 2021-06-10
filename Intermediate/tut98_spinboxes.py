from tkinter import * 

root = Tk()
root.title('Tkinter GUI - Sailendra')
root.geometry('400x400')

def grab():
    val = int(my_spin.get())
    my_label.config(text=val) 

my_spin = Spinbox(root, from_=0, to=10, font="Helvetica 20 bold", increment=2) 
# my_spin = Spinbox(root, values=('SAI', 'LEN', 'DRA', 'CHE', 'TTRI'), font="Helvetica 20 bold", increment=2) 
my_spin.pack(pady=20)

my_button = Button(root, text="Submit", command=grab)
my_button.pack(pady=20)

my_label = Label(root, text="")
my_label.pack(pady=20)

root.mainloop()