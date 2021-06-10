from os import stat
from tkinter import * 
from tkinter import filedialog
from tkinter.messagebox import showinfo

root = Tk()
root.title('Text Editor - Sailendra')

# Global valiable declearation beacuse it prevents from initial running
#Set variable for open file name
global open_status_name
open_status_name = False

global selected
selected = False

#Create new file function
def new_file():
    #Delete previous text
    my_text.delete("1.0", END)

    root.title("New File - TextPad!")
    status_bar.config(text="New file")

    #Set variable for open file name
    global open_status_name
    open_status_name = False

# Create open file function
def open_file():
    #Delete previous text
    my_text.delete("1.0", END)

    #Grab file name
    text_file = filedialog.askopenfilename(initialdir="/home/sailendrachettri/Learning /codes/Tkinter_CODEMY/Samples/", title="Open File", filetypes=(("Text Files", "*.txt"), ("HTML File", "*.html "), ("Python", "*.py"), ("All Files", "*.*")))
    
    #check to see if there is a file name
    if text_file:
        # make filename global so we can access 
        global open_status_name
        open_status_name = text_file

    #Update status bars
    name = text_file
    status_bar.config(text=f"{name}         ")
    name = name.replace("/home/sailendrachettri/Learning /codes/Tkinter_CODEMY/Samples/", "")
    root.title(f"{name} - TextPad!")  

    #Open the file
    text_file = open(text_file, 'r')
    stuff = text_file.read()

    #Add file to text box
    my_text.insert(END, stuff)

    # Close open file
    text_file.close() 

# Create save as file function
def save_as_file():
    text_file = filedialog.asksaveasfilename(defaultextension=".*", initialdir="/home/sailendrachettri/Learning /codes/Tkinter_CODEMY/Samples/", title="Save File", filetypes=(("Text Files", "*.txt"), ("HTML Files", ".html"), ("Python", ".py"), ("All Files", "*.*")))
    if text_file:
        #Update Status bar
        name = text_file
        status_bar.config(text=f" Saved: {name}         ")
        name = name.replace("/home/sailendrachettri/Learning /codes/Tkinter_CODEMY/Samples", "")
        root.title(f"{name} - TextPad!")  

        # Save the file
        text_file = open(text_file, 'w')
        text_file.write(my_text.get(1.0, END))
        text_file.close()

def save_file():
    global open_status_name
    if open_status_name:
        # Save the file
        text_file = open(open_status_name, 'w')
        text_file.write(my_text.get(1.0, END))
        text_file.close()

        #Put status update or popup code
        showinfo("File Saved", "Your file was saved to a directory!!")

        status_bar.config(text=f" Saved: {open_status_name}         ")
    else:
        save_as_file()

# Cut Text
def cut_text(e):
    global selected

    #Check to see if keyboard shortcut used
    if e:
        selecte= root.clipboard_get()
    else:
        if my_text.selection_get():
            # Grab selected text from text box
            selected = my_text.selection_get()

            #Delete selected text from text box
            my_text.delete("sel.first", "sel.last")  

            # Clear the clipboard and append
            root.clipboard_clear() 
            root.clipboard_append(selected) 

# Copy Text
def copy_text(e):
    global selected

    #Check to see if we used keyboard shortcut
    if e:
        selected = root.clipboard_get() 

    if my_text.selection_get():
        # Grab selected text from text box
        selected = my_text.selection_get() 

        # Clear the clipboard and append
        root.clipboard_clear() 
        root.clipboard_append(selected) 


# Paste Text
def paste_text(e):
    global selected

    #Check to see if keyboard shortcut is used
    if e:
        selected = root.clipboard_get()
    else:
        if selected:
            position = my_text.index(INSERT)
            my_text.insert(position, selected)

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

file_menu.add_command(label="New",command=new_file)
file_menu.add_command(label="Open", command=open_file)
file_menu.add_command(label="Save", command=save_file)
file_menu.add_command(label="Save As", command=save_as_file)
file_menu.add_separator() 
file_menu.add_command(label="Exit", command=quit)

# Add edit menu - submenu 2
edit_menu = Menu(my_menu, tearoff=False)
my_menu.add_cascade(label="Edit", menu=edit_menu)  

edit_menu.add_command(label="Cut                Ctrl + x", command=lambda: cut_text(False)) 
edit_menu.add_command(label="Copy               Ctrl + c", command=lambda: copy_text(False))
edit_menu.add_command(label="Paste              Ctrl + v", command=lambda: paste_text(False))
edit_menu.add_command(label="Undo               Ctrl + z")
edit_menu.add_command(label="Redo               Ctrl + y") 

# Add status bar to button of app
status_bar = Label(root, text="Ready         ", anchor=E)
status_bar.pack(fill=X, side=BOTTOM, ipadx=5) 

# Edit bindings
root.bind("<Control-Key-x>", cut_text)
root.bind("<Control-Key-c>", copy_text)
root.bind("<Control-Key-v>", paste_text)

root.mainloop()