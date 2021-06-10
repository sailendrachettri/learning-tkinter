from tkinter import * 

root = Tk()
root.title('Tkinter GUI - Sailendra')
root.geometry('400x400')

def button_hover(event):
    my_button["bg"] = "white"
    status_label.config(text="I am hovering over the buttom!")

def button_hover_leave(event):
    my_button["bg"] = "grey"
    status_label.config(text="")


my_button = Button(root, text="Click Me", font="Courier 20")
my_button.pack(pady=30)

status_label = Label(root, text="", relief=SUNKEN, anchor=E)
status_label.pack(fill=X, side=BOTTOM, ipady=2)

my_button.bind("<Enter>", button_hover)
my_button.bind("<Leave>", button_hover_leave)

root.mainloop()