from tkinter import * 
from tkinter import ttk

root = Tk()
root.title('Tkinter GUI - Sailendra')
# root.geometry('400x400')

my_notebook = ttk.Notebook(root)
my_notebook.pack()


#Hide function
def hide():
    my_notebook.hide(1)

#Show function
def show():
    my_notebook.add(my_frame2, text="Red Tab")

#Select/navigate function
def select():
    my_notebook.select(1)

# Creating frames
my_frame1 = Frame(my_notebook, width=500, height=500, bg='blue')
my_frame1.pack(fill=BOTH, expand=True)
my_frame2 = Frame(my_notebook, width=500, height=500, bg='red')
my_frame2.pack(fill=BOTH, expand=True) 

#Adding frames in tab
my_notebook.add(my_frame1, text="Blue tab")
my_notebook.add(my_frame2, text="Red tab")

#Create button hide tab
my_button = Button(my_frame1, text="Hide tab 2", command=hide)
my_button.pack(pady=10)

#Show a tab
my_button2 = Button(my_frame1, text="Show tab 2", command=show)
my_button2.pack(pady=10)

#navigate to tab 2
my_button3 = Button(my_frame1, text="Go to tab 2", command=select)
my_button3.pack(pady=10)

root.mainloop()