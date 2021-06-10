from tkinter import * 

root = Tk()
root.title('Tkinter GUI - Sailendra')
root.geometry('400x400')

my_menu = Menu(root)
root.config(menu=my_menu) 

def our_command():
    pass


# Creat a menu item
file_menu = Menu(my_menu)
my_menu.add_cascade(label="File", menu=file_menu) 
file_menu.add_command(label="New File", command=our_command)
file_menu.add_separator()
file_menu.add_command(label="Exit", command=root.quit)

# Create an edit menu item
edit_menu = Menu(my_menu)
my_menu.add_cascade(label="Edit", menu=edit_menu)
edit_menu.add_command(label="Cut", command=our_command) 
edit_menu.add_command(label="Copy", command=our_command)

run_menu = Menu(my_menu)
my_menu.add_cascade(label="Run", menu=run_menu)
run_menu.add_command(label="Start", command=our_command) 
run_menu.add_command(label="Stop", command=our_command)



root.mainloop() 