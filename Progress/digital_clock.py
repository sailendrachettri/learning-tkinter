import time
from tkinter import *
from PIL import Image
from PIL.ImageTk import PhotoImage

root = Tk()
root.title('Digital Clock - Sailendra')
root.geometry("600x650")
root.configure(bg="#0075A2")

#A function for clock
def clock():
    hour = time.strftime("%I")
    minute = time.strftime("%M")
    second = time.strftime("%S")
    am_pm = time.strftime("%P")

    clock_label.config(text=hour + ":" + minute + ":" + second + " " + am_pm) 
    clock_label.after(1000, clock) # it call clock function in every 1 seconds

#Background image
image = Image.open("img/digital_clock.png")
resized = image.resize((500, 500), Image.ANTIALIAS)
new_image = PhotoImage(resized)
image_label = Label(root, image=new_image, bg="#0075A2")
image_label.grid(row=0, column=0,pady=40, padx=(40, 0))

#Create label to display watch's text
clock_label = Label(root, text="10:20:20 Am", font="Helvetica 46 bold", bg='white', fg='red') 
clock_label.grid(row=0, column=0, padx=(40, 0))

#Calling the function
clock()

root.mainloop()
