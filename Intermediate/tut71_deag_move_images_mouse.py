from tkinter import * 

root = Tk()
root.title('Tkinter GUI - Sailendra')
root.geometry('600x500')

w = 600
h = 400
x = w//2
y = h//2

my_canvas = Canvas(root, width=w, height=h, bg="white")
my_canvas.pack(pady=15)  

# Add image to the canvas
img = PhotoImage(file="img/sailendra.png") 
my_image = my_canvas.create_image(100, 100, anchor=NW, image=img) 

def move(event):
    global img
    img = PhotoImage(file="img/sailendra.png") 
    my_image = my_canvas.create_image(event.x, event.y, image=img) 
    my_label.config(text="Coordinates x: " + str(event.x) + " y: " + str(event.y))

# root.bind("<Left>", left)
# root.bind("<Right>", right)
# root.bind("<Up>", up)
# root.bind("<Down>", down)

my_label = Label(root, text="")
my_label.pack(pady=20)

# my_canvas.bind("<Motion>", move) 
my_canvas.bind("<B1-Motion>", move) 

root.mainloop()