from tkinter import * 

root = Tk()
root.title('Tkinter GUI - Sailendra')
root.geometry('400x400')

def myClick():
    hello = "Hello " + e.get()
    mylabel = Label(root, text=hello)
    e.delete(0, END)
    mylabel.pack(pady=10, padx=10)

    



e = Entry(root, width=50, font="Helvetica 20 bold")
e.pack(padx=10, pady=10)

my_button = Button(root, text="Enter name", command=myClick)
my_button.pack(padx=10, pady=10)


root.mainloop()