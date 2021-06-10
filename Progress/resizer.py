from tkinter import * 

root = Tk()
root.title("Tkinter Resizer - Sailendra")
root.geometry('250x200')
root.configure(background="#F4A261")

# Creating new window
top = Toplevel()
top.configure(background="#CB04A5")
top.title("Resizing....")

# Function where we put width and height
def resize_window(*args): 
    top.geometry(f"{width.get()}x{height.get()}") 

# Displaying label text in root window
Label(root, text="Width: ", font="courier 20 bold", bg='#F4A261').grid(row=0, column=0, pady=30)
Label(root, text="Height: ", font="courier 20 bold", bg='#F4A261').grid(row=1, column=0, pady=30)

# Scale silder provides graphical slider where we set the value of width and height
width = Scale(root, from_=100, to=800, command=resize_window, orient=HORIZONTAL, width=20, bg='#F4A261')
height = Scale(root, from_=100, to=800, command=resize_window, orient=HORIZONTAL, width=20, bg='#F4A261')
width.grid(row=0, column=1)
height.grid(row=1, column=1)



root.mainloop()