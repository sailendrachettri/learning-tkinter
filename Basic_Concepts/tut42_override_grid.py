from tkinter import * 

root = Tk()
root.title('Tkinter GUI - Sailendra')
root.geometry('400x400')

myLabel = Label(root)

def myClick():
    global myLabel
    myLabel.destroy() 

    hello = "Hello "+ e.get()
    myLabel = Label(root, text=hello)
    myLabel.grid(row=3, column=0, pady=10)
    

e = Entry(root, width=17, font="Helvetica 30")
e.grid(row=0, column=0, padx=10, pady=10)

my_button = Button(root, text="Enter your name: ", command=myClick)
my_button.grid(row=1, column=0, pady=10)


root.mainloop()