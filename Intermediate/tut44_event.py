from tkinter import * 

root = Tk()
root.title('Tkinter GUI - Sailendra')
root.geometry('400x400')

def clicker(event):
    myLabel = Label(root, text="You clicked a button"+ event.keysym)
    myLabel.pack() 

myButton = Button(root, text="Click me")
# myButton.bind('<Button-3>', clicker)  
# myButton.bind('<Enter>', clicker)  
# myButton.bind('<FocusIn>', clicker)  
# myButton.bind('<FocusOut>', clicker)  
# myButton.bind('<Return>', clicker)  
# myButton.bind('<Key>', clicker)  
myButton.bind('<Key>', clicker)  
myButton.pack(pady=20)


root.mainloop()