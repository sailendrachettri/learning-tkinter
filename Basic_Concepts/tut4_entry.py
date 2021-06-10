from tkinter import * 

root = Tk()

# Entry(root, width=50, bg='orange', fg='white', borderwidth=5).pack()
e = Entry(root, width=50)
e.pack()
e.insert(0, "Enter Your Quote: ")

def myClick():
    var = "Hello " + e.get()
    Label(root, text=var).pack()

myButton = Button(root, command=myClick, text="Click Me!", padx=50, pady=50, fg="white", bg="#000000") 
myButton.pack()


root.mainloop()