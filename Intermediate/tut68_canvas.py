from tkinter import * 

root = Tk()
root.title('Tkinter GUI - Sailendra')
root.geometry('400x400')

my_canvas = Canvas(root, width=300, height=200, bg='white')
my_canvas.pack(pady=20)

# Creact rectangle
# my_canvas.create_rectangle(x1, y1, x2, y2, fill='pink')
# Rectangle x1, y1: Top left
# Rectangle x2, y2: Buttom right
my_canvas.create_rectangle(50, 150, 250, 50, fill='pink')

# Create Line
# my_canvas.create_line(x1, y1, x2, y2, fill='color')
my_canvas.create_line(0, 100, 300, 100, fill='red')
my_canvas.create_line(150, 0, 150, 200, fill='red')


# Create Oval
# my_canvas.create_oval(x1, y1, x2, y2, fill='pink')
# Oval x1, y1: Top left
# Oval x2, y2: Buttom right
my_canvas.create_oval(50, 150, 250, 50, fill='cyan')


root.mainloop()