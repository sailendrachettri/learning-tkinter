import random
from tkinter import *
from string import ascii_letters, digits, punctuation


root = Tk()
root.title('Strong Password Generator - Sailendra')
root.geometry('700x500')
root.configure(background='#19647E')


#Create a function to display password in screen
def diaplay_password():
    password_length = digit_scale.get()

    # We join them with an empty string so the sequence becomes a string
    random_password = ''.join(random.choices(ascii_letters + digits + punctuation, k=password_length))    

    # Configure to display password on screen
    display_password.config(text= "Password: " + random_password)
    

#Create a Label for heading
heading_label = Label(root, text='Strong Password Generator', font="cursive 26 bold", anchor=CENTER, bg='#19647E')
heading_label.pack(pady=50)

#Create slider to set number digits
digit_scale = Scale(root, from_=5, to=32, orient=HORIZONTAL, width=50,  font='courier 30', activebackground='#19647E', bd=1, length=360, relief=SUNKEN, sliderlength=70, troughcolor='#FFE3E3', bg='#19647E', fg='white')
digit_scale.pack()

# Create button to generate random number
generate_button = Button(root, text="Generate", command=diaplay_password, font="Cursive 20", bg='#19647E', fg='white')
generate_button.pack(pady=40)

# Create a Label to display password to the screen
display_password = Label(root, text="", font="Helvetica 20", bg='#19647E', fg='#EEEEEE')
display_password.pack()

root.mainloop()