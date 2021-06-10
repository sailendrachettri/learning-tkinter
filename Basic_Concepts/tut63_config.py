from tkinter import * 

root = Tk()
root.title('Tkinter GUI - Sailendra')
root.geometry('400x400')

def something():
    my_label.config(text="This is new text") 
    root.config(bg='blue') 
    my_button.config(text="clicked!", state=DISABLED)

global my_label
my_label = Label(root, text="Text text", font="Courier 20 bold")
my_label.pack(pady=20)

global my_button
my_button = Button(root, text="Click me", command=something)
my_button.pack(pady=10) 


root.mainloop()