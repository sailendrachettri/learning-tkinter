from tkinter import * 

root = Tk()
root.title('Text Editor - Sailendra')
# root.geometry('400x400')


#Create main frame
my_frame = Frame(root)
my_frame.pack(pady=5)

#Create our scrollbar for the text box
text_scroll = Scrollbar(my_frame)
text_scroll.pack(side=RIGHT, fill=Y)

#Create text box
my_text = Text(my_frame, width=97, height=25, font="Courier 16", selectbackground="yellow", selectforeground="black", undo=TRUE, yscrollcommand=text_scroll.set)
my_text.pack()

#Configure our scrollbar
text_scroll.config(command=my_text.yview)

#Create menu
my_menu = Menu(root)
root.config(menu=my_menu)

# Add file menu - submenu 1
file_menu = Menu(my_menu, tearoff=False)
my_menu.add_cascade(label="File", menu=file_menu)  

file_menu.add_command(label="New")
file_menu.add_command(label="Open")
file_menu.add_command(label="Save")
file_menu.add_separator() 
file_menu.add_command(label="Exit", command=quit)

# Add edit menu - submenu 2
edit_menu = Menu(my_menu, tearoff=False)
my_menu.add_cascade(label="Edit", menu=edit_menu)  

edit_menu.add_command(label="Cut            ctrl+x")
edit_menu.add_command(label="Copy           ctrl+c")
edit_menu.add_command(label="Paste          ctrl+v")
edit_menu.add_command(label="Undo           ctrl+z")
edit_menu.add_command(label="Redo           ctrl+y") 

# Add status bar to button of app
status_bar = Label(root, text="Ready", anchor=E)
status_bar.pack(fill=X, side=BOTTOM, ipadx=5) 

root.mainloop()