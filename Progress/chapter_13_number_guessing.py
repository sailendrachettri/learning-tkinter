from tkinter import * 
from random import randint
from tkinter.messagebox import showwarning, showinfo

root = Tk()
root.title('Number Guessing Game - Sailendra')
root.geometry('770x600')
root.configure(bg="#058ED9")

#Declear number of chances a user have
global count 
count = 10

#Check value function
def check_value():
    global count

    try:
        user_value = int(spinbox.get())
        random_value = randint(0, 10)
        # print(random_value) # for debug

        if user_value < random_value:
            display_label.config(text="Your number is bigger")

        elif user_value == random_value:
            display_label.config(text="Correct Guess")
            showinfo("You win the game", "Congratulation you win.")
            display_label.config(text="Welcome to the Game")
            count = 11

            check_button.config(state=DISABLED)
            reset_button.config(state=DISABLED)
        
        else:
            display_label.config(text="Your number is smaller")
    except:
        showwarning("Invalid Input", "Please try to change your input.")

    # Clear spinbox's value
    spinbox.delete(0, END)

    count -= 1
    count_label.config(text=f"Remaning Chances {count}")

    # If count is less than 0 you lose the game
    if count <= 0:
        showwarning("You lose", "You lose the game\nTry again!")
        quit() 
        


# Game start function
def start_game():
    global check_button, reset_button
    display_label.config(text="Try to guess number between 0 to 10")
    check_button.config(activebackground="#058ED9", activeforeground="#EEEEEE", state=ACTIVE) 
    reset_button.config(activebackground="#058ED9", activeforeground="#EEEEEE", state=ACTIVE)



# Game restart
def reset_game():
    reset_button.config(state=DISABLED)
    check_button.config(state=DISABLED)
    global count
    count = 10
    count_label.config(text=f"Remaning Chances {count}")

# Create frames
heading_frame = Frame(root, bg="#058ED9")
heading_frame.pack(pady=10)

# packing below two frames in this frame
display_spinbox_checkbtn = Frame(root, bd=2, relief=SUNKEN, bg="#058ED9", pady=10, padx=10)
display_spinbox_checkbtn.pack(pady=10, ipadx=100)

display_frame = Frame(display_spinbox_checkbtn, bg="#058ED9")
display_frame.pack(pady=10) 

spinbox_checkbutton_frame = Frame(display_spinbox_checkbtn, bg="#058ED9")
spinbox_checkbutton_frame.pack(pady=10)

start_reset_frame = Frame(root, bg="#058ED9")
start_reset_frame.pack() 

count_frame = Frame(root, bg="#058ED9")
count_frame.pack()

# Create heaing
heading_label = Label(heading_frame, text="Number Guessing Game", fg="#EEEEEE", bg="#058ED9", font=("Times New Roman", 30, "bold"))
heading_label.pack(pady=20) 

# Create display label
display_label = Label(display_frame, text="Welcome to the Game", bg="#058ED9", font=("Times New Roman", 23), fg="#EEEEEE", pady=10, padx=10, bd=2, relief=SUNKEN)
display_label.pack(pady=10, padx=10)

# Create spinbox to enter number
spinbox = Spinbox(spinbox_checkbutton_frame, from_=0, to=10, width=6, font=("Times New Roman", 40, "bold"), justify=CENTER)
spinbox.grid(row=0, column=0, pady=20) 

# Check button
global check_button
check_button = Button(spinbox_checkbutton_frame, text="Check", state=DISABLED, font=("Times New Roman", 25), bg="#058ED9", fg="#EEEEEE", command=check_value)
check_button.grid(row=1, column=0, pady=(10, 20))

# Start button
start_button = Button(start_reset_frame, text="Start", font=("Times New Roman", 25), bg="#058ED9", fg="#EEEEEE", command=start_game)
start_button.grid(row=0, column=0, pady=10, padx=10)

# Reset button
global reset_button
reset_button = Button(start_reset_frame, text="Reset", state=DISABLED, font=("Times New Roman", 25), bg="#058ED9", fg="#EEEEEE", command=reset_game)
reset_button.grid(row=0, column=1)

# Remaining chances
count_label = Label(count_frame, text="Remaining Chances 10", font=("Times New Roman", 16), bg="#058ED9", fg="#EEEEEE")
count_label.pack(pady=7) 

root.mainloop()