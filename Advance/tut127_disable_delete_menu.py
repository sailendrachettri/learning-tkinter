from tkinter import * 

root = Tk()
root.title('Tkinter GUI - Sailendra')
root.geometry('400x400')

def new():
    pass

def open():
    pass

def disable_new():
    # file_menu.entryconfig("New", state=DISABLED) 
    my_menu.entryconfig("File", state=DISABLED) 

def enable_new():
    # file_menu.entryconfig("New", state=NORMAL) 
    my_menu.entryconfig("File", state=NORMAL) 

def delete_new():
    # file_menu.delete("New")
    my_menu.delete("File")

my_menu = Menu(root)
root.config(menu=my_menu)

# Add menu items
file_menu = Menu(my_menu, tearoff=False)
edit_menu = Menu(my_menu, tearoff=False) 
my_menu.add_cascade(label="File", menu=file_menu) 
my_menu.add_cascade(label="Edit", menu=edit_menu)  

# Add dropdowns
file_menu.add_command(label="New", command=new)
file_menu.add_command(label="Open", command=open)

edit_menu.add_command(label="Undo", command=new)
edit_menu.add_command(label="Redo", command=open) 

# Create buttons
disable_button = Button(root, text="DISABLE", command=disable_new)
disable_button.pack(pady=40)

enable_button = Button(root, text="ENABLE", command=enable_new)
enable_button.pack(pady=40)

delete_button = Button(root, text="DELETE", command=delete_new)
delete_button.pack(pady=40)

root.mainloop()