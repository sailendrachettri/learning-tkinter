from tkinter import * 
from tkinter import messagebox


root = Tk()
root.title("Message Box") 
root.geometry("400x400")

#showinfo, showwarning, showerror, askquestion, askokcancel, askyesno
def popup():
    # response =  messagebox.showinfo("Popup", "Hello World!")
    # response =  messagebox.showwarning("Popup", "Hello World!")
    # response =  messagebox.showerror("Popup", "Hello World!")
    # response =  messagebox.askquestion("Popup", "Hello World!")
    # response =  messagebox.askokcancel("Popup", "Hello World!")
    response =  messagebox.askyesno("Popup", "Hello World!")

    if response == 1:
        Label(root, text="You clicked OK!").pack()
    else:
        Label(root, text="You clicked Cancle!").pack()

    Label(root, text=response).pack()
    

Button(root, text="Popup", command=popup).pack()


root.mainloop()