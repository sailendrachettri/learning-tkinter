from tkinter import *

root = Tk()
root.title('Tkinter GUI - Sailendra')

# Designate Height and Width of our app
app_width = 500
app_height = 500

screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()

x = (screen_width / 2) - (app_width/2)
y = (screen_height / 2) - (app_height/2)

# width x height + x-axis + y-axis
root.geometry(f'{app_width}x{app_height}+{int(x)}+{int(y)}')
# root.geometry("2732x768")

my_label = Label(root, text=f"Width: {screen_width} Height: {screen_height}")
my_label.pack(pady=10)


root.mainloop()
