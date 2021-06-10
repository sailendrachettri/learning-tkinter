from tkinter import *
import random

root = Tk()
root.title("Dice Simulator")
root.geometry("600x500")

def roll_dice():
    dice = ['\u2680', '\u2681', '\u2682', '\u2683', '\u2684', '\u2685'] 

    random_value = random.choice(dice)
    label.config(text=random_value)  

# Create unicode dice
label = Label(root, text="", font="Courier 85 bold")
label.pack()

# create button
button = Button(root, text="Dice Roll", font="Courier 20 bold",command=roll_dice)
button.pack()


root.mainloop() 


