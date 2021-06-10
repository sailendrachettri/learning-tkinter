from tkinter import * 
from random import choice

root = Tk()
root.title('Tkinter GUI - Sailendra')
root.geometry('700x500')
root.configure(bg="#044389")

def dice_simulator():
    dice = ['\u2680', '\u2681', '\u2682', '\u2683', '\u2684', '\u2685'] 

    # Configure dice 
    dice_one.config(text=f'{choice(dice)}')
    dice_two.config(text=f'{choice(dice)}')
    dice_three.config(text=f'{choice(dice)}')
    dice_four.config(text=f'{choice(dice)}')
    dice_five.config(text=f'{choice(dice)}')
    dice_six.config(text=f'{choice(dice)}')

#Create frames for heading, 'dice(s) & button' and one extra to pack dice_frame and button_frame
heading_frame = Frame(root, bg="#044389")
heading_frame.pack(pady=10)

#Pack dice_frame and button_frame in this frame 
dice_button_frame = Frame(root, bg="#044389", bd=2, relief=RAISED, pady=30, padx=20)
dice_button_frame.pack()

dice_frame = Frame(dice_button_frame, bg="#044389")
dice_frame.pack(pady=10)

button_frame = Frame(dice_button_frame, bg="#044389")
button_frame.pack(pady=10)


#Create a label for heading text
heading_label = Label(heading_frame, text="Dice Simulator", font=("Times New Roman", "35", "bold"), bg="#044389", fg="#EEEEEE")
heading_label.pack(pady=20)

# Create six Labels for dice(s)
dice_one = Label(dice_frame, text="\u2680", font="Courier 100", bg="#044389", fg="#EEEEEE")
dice_one.grid(row=0, column=0, padx=5)

dice_two = Label(dice_frame, text="\u2681", font="Courier 100", bg="#044389", fg="#EEEEEE")
dice_two.grid(row=0, column=1, padx=5)

dice_three = Label(dice_frame, text="\u2682", font="Courier 100", bg="#044389", fg="#EEEEEE")
dice_three.grid(row=0, column=2, padx=5)

dice_four = Label(dice_frame, text="\u2683", font="Courier 100", bg="#044389", fg="#EEEEEE")
dice_four.grid(row=0, column=3, padx=5)

dice_five = Label(dice_frame, text="\u2684", font="Courier 100", bg="#044389", fg="#EEEEEE")
dice_five.grid(row=0, column=4, padx=5)

dice_six = Label(dice_frame, text="\u2685", font="Courier 100", bg="#044389", fg="#EEEEEE")
dice_six.grid(row=0, column=5, padx=5)

# Create a button to roll dice
roll_dice_button = Button(button_frame, text="Roll Dice", font=("Times New Roman", "25"), bg="#044389", fg="#EEEEEE" ,command=dice_simulator)
roll_dice_button.pack(ipadx=30) 


root.mainloop()