from tkinter import * 

root = Tk()
root.title('Tkinter GUI - Sailendra')
root.geometry('400x400')

# my_menu = Menu(root)
# root.config(menu=my_menu) 

def our_command():
    pass

# File new function
def file_new_command():
    hide_all_frames()
    file_new_frame.pack(fill=BOTH, expand=True)
    my_label = Label(file_new_frame, text="You clicked a dropdown menu!").pack()

#Create edit function
def edit_cut_command():
    hide_all_frames()
    edit_cut_frame.pack(fill=BOTH, expand=True)
    my_label = Label(edit_cut_frame, text="You clicked a dropdown menu!").pack()

#hide all frame functions
def hide_all_frames():
    file_new_frame.pack_forget()
    edit_cut_frame.pack_forget()
    
'''
# Creat a menu item 
file_menu = Menu(my_menu)
my_menu.add_cascade(label="File", menu=file_menu) 
file_menu.add_command(label="New File", command=file_new_command)
file_menu.add_separator()
file_menu.add_command(label="Exit", command=root.quit)

# Create an edit menu item
edit_menu = Menu(my_menu)
my_menu.add_cascade(label="Edit", menu=edit_menu)
edit_menu.add_command(label="Cut", command=edit_cut_command) 
edit_menu.add_command(label="Copy", command=our_command)

run_menu = Menu(my_menu)
my_menu.add_cascade(label="Run", menu=run_menu)
run_menu.add_command(label="Start", command=our_command) 
run_menu.add_command(label="Stop", command=our_command)
'''
# Create some frames
file_new_frame = Frame(root, width=400, height=400, bg='red')

edit_cut_frame = Frame(root, width=400, height=400, bg='blue')

root.mainloop() 