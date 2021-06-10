from tkinter import * 
from tkinter import ttk 

root = Tk()
root.title('Tkinter GUI - Sailendra')
root.geometry('400x400')

#Create a main frame
main_frame = Frame(root)
main_frame.pack(fill=BOTH, expand=True)

#create a canvas
my_canvas = Canvas(main_frame)
my_canvas.pack(side=LEFT, fill=BOTH, expand=1)

#add a scrollbar to the canvas
my_scrollbar = ttk.Scrollbar(main_frame, orient=VERTICAL, command=my_canvas.yview)
my_scrollbar.pack(side=RIGHT, fill=Y) 

#configure the canvas
my_canvas.configure(yscrollcommand=my_scrollbar.set)
my_canvas.bind('<Configure>', lambda e: my_canvas.configure(scrollregion=my_canvas.bbox("all"))) 

#create another frame inside the canves
second_frame = Frame(my_canvas)

#add that new frame to a window in the canvas
my_canvas.create_window((0,0,), window=second_frame, anchor=NW) 

for thing in range(100):
    Button(second_frame, text=f"Button {thing} Yo!").grid(row=thing, column=0, pady=10, padx=10)


root.mainloop() 