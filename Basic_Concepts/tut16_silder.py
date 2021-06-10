from tkinter import * 

root = Tk()
root.title("Slider in TKinter")
root.geometry("400x400")

vertical = Scale(root, from_=0, to=1000)
vertical.pack() 

# def btn():
#     my_label = Label(root, text=vertical.get()).pack()


horizontal = Scale(root, from_=0, to=1000, orient = HORIZONTAL)
horizontal.pack() 

# def btn():
#     my_label = Label(root, text=horizontal.get()).pack()


def resize():
    root.geometry(f"{horizontal.get()}x{vertical.get()}") 

val = Button(root, text="Resize", command=resize).pack()

root.mainloop()