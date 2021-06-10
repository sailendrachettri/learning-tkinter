from tkinter import *
import time

root = Tk()
root.title('Tkinter GUI - Sailendra')
root.geometry('400x400')


def clock():
    hour = time.strftime("%H") # I FOR 12 HOUR
    minute = time.strftime("%M")
    second = time.strftime("%S") 
    day = time.strftime("%A") 
    am_pm = time.strftime("%p") 

    my_label.config(text=hour + ":" + minute + ":" + second+ " " + am_pm)
    my_label.after(1000, clock) 

    my_label2.config(text=day)


my_label = Label(root, text="", font="Courier 20 bold", bg="black", fg="blue")
my_label.pack(pady=20) 

my_label2 = Label(root, text="", font="Helvetica 14 bold", bg="black", fg="red")
my_label2.pack(pady=10) 

#Rough
# def update():
#     my_label.config(text="New text") 
# my_label.after(5000, clock)  #5 sec == 5000 milisec

clock()


root.mainloop()