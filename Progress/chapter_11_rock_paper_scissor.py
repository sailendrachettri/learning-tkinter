from tkinter import * 
from random import randint
from tkinter.messagebox import showwarning

root = Tk()
root.title('Game in Python - Sailendra')
root.geometry('600x500')
root.configure(bg="#006D77")

user_score = 10
comp_score = 10

def rock_paper_scissor(choice):
    rock = 1
    paper = 2
    scissor = 3
    
    computer_choice = randint(1, 3)
    user_choice = choice

    # Retaining score value till the program is running
    global comp_score
    global user_score

    if  (computer_choice == rock and user_choice == scissor) or \
        (computer_choice == paper and user_choice == rock) or \
        (computer_choice == scissor and user_choice == paper):
        win_at_a_time.config(text='Computer Win')
        computer_score_label.config(text=f"Computer Score: {comp_score}")
        comp_score += 10
        
    elif (user_choice == rock and computer_choice == scissor) or \
         (user_choice == paper and computer_choice == rock) or \
         (user_choice == scissor and computer_choice == paper):
         win_at_a_time.config(text='You win') 
         your_score_label.config(text=f"Your Score: {user_score}")
         user_score += 10
        
    else:
        win_at_a_time.config(text="Draw")



#frames for heading, body content and output
heading_frame = Frame(root, bg="#006D77")
heading_frame.pack()

body_frame = Frame(root, bg="#006D77")
body_frame.pack(pady=30)

output_frame = Frame(root, bg="#006D77")
output_frame.pack(pady=30)

# Heading label text
heading_label = Label(heading_frame, text="Rock Paper Scissor", font=("Times New Roman", "30", "bold"), fg="#EEEEFF",bg="#006D77") 
heading_label.pack(pady=30)

# Create three button for rock, paper, scissor
rock_button = Button(body_frame, text="Rock", command=lambda : rock_paper_scissor(1), font=("Times New Roman", "20"), bg="#006D77", fg="#EEEEFF")
rock_button.grid(row=0, column=0)

rock_button = Button(body_frame, text="Paper", command=lambda : rock_paper_scissor(2), font=("Times New Roman", "20"), bg="#006D77", fg="#EEEEFF")
rock_button.grid(row=0, column=1, padx=(0, 60))

rock_button = Button(body_frame, text="Scissor", command=lambda : rock_paper_scissor(3), font=("Times New Roman", "20"), bg="#006D77", fg="#EEEEFF")
rock_button.grid(row=0, column=2)

# Score label for computer and your
your_score_label = Label(body_frame, text="Your Score: 0", font=("Times New Roman", "20"), bg="#006D77", fg="#EEEEFF")
your_score_label.grid(row=1, column=0, sticky=W, pady=(40, 0))
computer_score_label = Label(body_frame, text="Computer Score: 0", font=("Times New Roman", "20"), bg="#006D77", fg="#EEEEFF")
computer_score_label.grid(row=2, column=0, sticky=W)

win_at_a_time = Label(output_frame, text="", font=("Times New Roman", "20"), bg="#006D77", fg="#EEEEFF")
win_at_a_time.pack(pady=10)

root.mainloop()