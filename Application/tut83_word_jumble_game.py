from tkinter import * 
from random import choice
from random import shuffle

root = Tk()
root.title('Tkinter GUI - Sailendra')
root.geometry('500x400')

my_label = Label(root, text="starting..", font="courier 20")
my_label.pack(pady=20)

def shuffler():
    #clear answer box and label
    entry_answer.delete(0, END)
    answer_label.config(text='')
    states = ['Washington', 'Oregon', 'California', 'Ohio', 'Nebraska', 'Colorado', 'Michigan', 'Massachusetts', 'Florida', 'Texas', 'Oklahoma', 'Hawaii', 'Alaska', 'Utah', 'New Mexico', 'North Dakota', 'South Dakota', 'West Virginia', 'Virginia', 'New Jersey', 'Minnesota', 'Illinois', 'Indiana', 'Kentucky', 'Tennessee', 'Georgia', 'Alabama', 'Mississippi', 'North Carolina', 'South Carolina', 'Maine', 'Vermont', 'New Hampshire', 'Connecticut', 'Rhode Island', 'Wyoming', 'Montana', 'Kansas', 'Iowa', 'Pennsylvania', 'Maryland', 'Missouri', 'Arizona', 'Nevada', 'New York', 'Wisconsin', 'Delaware', 'Idaho', 'Arkansas', 'Louisiana']


    #Pick random fruits name
    global word
    word = choice(states)

    #Break apart our chosen word
    break_apart_word = list(word)
    shuffle(break_apart_word)

    #Turn shuffeled list into a word
    global shuffled_word

    shuffled_word = ''
    for letter in break_apart_word:
        shuffled_word += letter
    
    # Print shuffle word to the screen
    my_label.config(text=shuffled_word)
    
# Create answer function
def answer():
    if word == entry_answer.get():
        answer_label.config(text="Correct!!")
    else:
        answer_label.config(text="Incorrect!!")
        

global entry_answer
entry_answer = Entry(root, text="Courier 20")
entry_answer.pack(pady=20)

button_frame = Frame(root)
button_frame.pack(pady=20)

my_button = Button(button_frame, text="Pick another word", command=shuffler) 
my_button.grid(row=0, column=0,pady=20)

answer_button = Button(button_frame, text="Answer", command=answer)
answer_button.grid(row=0, column=1) 

answer_label = Label(root, text='', font="Courier 20")
answer_label.pack(pady=10) 

root.mainloop()