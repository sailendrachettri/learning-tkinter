from tkinter import * 

root = Tk()
root.title('Tkinter GUI - Sailendra')
root.geometry('400x400')

def grab():
    my_label.config(text=my_box.get())

my_box = Entry(root, font="Courier 20 bold")
my_box.pack(pady=10)

my_button = Button(root, text="Grab Text From box", command=grab).pack(pady=20) 


my_label = Label(root, text="").pack(pady=20)


root.mainloop()