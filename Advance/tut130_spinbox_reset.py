from tkinter import * 

root = Tk()
root.title('Tkinter GUI - Sailendra')
root.geometry('400x400')

def reset():
    # var = IntVar(root) 
    # var.set(0)

    # my_spin.config(textvariable=var)

    var2 = StringVar(root) 
    var2.set("John")
    my_spin.config(textvariable=var2)
    

# Set Integer variable
var = IntVar(root) 
var.set(20)

# Set String variable
var2 = StringVar(root) 
var2.set("John")

# For integer
# my_spin = Spinbox(root, from_=0, to=100, font=("Times New Roman", 25), textvariable=var) 
# my_spin.pack(pady=20)

# For string
my_spin = Spinbox(root, values=("Sailendr", "Chettri", "Mina"), font=("Times New Roman", 25), textvariable=var) 
my_spin.pack(pady=20)

my_button = Button(root, text="Reset Spinner", command=reset)
my_button.pack(pady=20)


root.mainloop()