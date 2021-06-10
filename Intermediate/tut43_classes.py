from tkinter import * 

root = Tk()
root.title('Tkinter GUI - Sailendra')
root.geometry('400x400')

class Elder:
    def __init__(self, master):
        myFrame = Frame(master) 
        myFrame.pack()

        self.myButton = Button(master, text="Click me", command=self.clicker) 
        self.myButton.pack(pady=20) 
        
    def clicker(self):
        print("Look at you...") 

e = Elder(root)  

root.mainloop()