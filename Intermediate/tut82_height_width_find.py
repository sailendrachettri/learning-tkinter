from tkinter import * 

root = Tk()
root.title('Tkinter GUI - Sailendra')
# root.geometry('400x400')

def info():
    dimension_label = Label(root, text=root.winfo_geometry()) 
    dimension_label.pack(pady=20)

    height_label = Label(root, text="Height" + str(root.winfo_height()))
    height_label.pack(pady=20)

    width_label = Label(root, text="width" + str(root.winfo_width()))
    width_label.pack(pady=20)

    x_label = Label(root, text="X" + str(root.winfo_x()))
    x_label.pack(pady=20)

    y_label = Label(root, text="Y" + str(root.winfo_y()))
    y_label.pack(pady=20)

my_button = Button(root, text="Click Me", command=info)
my_button.pack(pady=20)

root.mainloop()