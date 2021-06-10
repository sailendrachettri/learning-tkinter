from tkinter import * 

root = Tk()
root.title('Tkinter GUI - Sailendra')
root.geometry('400x400')

def myDelete():
    if myLabel.winfo_exists() == 1:
        pass
    else:
        pass
    
    myLabel.pack_forget()  # we can bring back if we want
    myLabel.destroy()  # deletes it forever
    my_button['state'] = NORMAL


def myClick():
    global myLabel
    hello = "Hello "+ e.get()
    myLabel = Label(root, text=hello)
    myLabel.pack(pady=10)
    my_button['state'] = DISABLED
    print(my_button.winfo_exists())


e = Entry(root, width=50, font="Helvetica 30")
e.pack(padx=10, pady=10)

my_button = Button(root, text="Enter your name: ", command=myClick)
my_button.pack(pady=10)

delete_button = Button(root, text="Delete text", command=myDelete)
delete_button.pack(pady=10)

root.mainloop()