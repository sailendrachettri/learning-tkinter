from tkinter import *
from PIL import Image, ImageTk
from random import randint

root = Tk()
root.title('Tkinter GUI - Sailendra')
root.geometry('500x500')

#Create randomizing state function
def random_state():
    #Create a list of state names
    global our_states
    our_states = ['california', 'florida', 'illinois', 'kentucky', 'texas', 'hawaii'] #1 means california, 2 means florida etc

    #Generate a random number
    global rando
    rando = randint(0, len(our_states)-1)
    state = "img/flashcard/" + our_states[rando] + '.png' 

    #Creat state image 
    global state_image 
    state_image = ImageTk.PhotoImage(Image.open(state)) 
    show_state.config(image=state_image)


#Create answer function
def state_answer():

    answer = answer_input.get()
    answer = answer.replace(" ", "")

    # Determine if our answer is right or wrong
    if answer.lower() == our_states[rando]:
        response = "Correct" + our_states[rando].title()

    else:
        response = "Incorrect" + our_states[rando].title() 

    answer_label.config(text=response)  

    
    #Create the entry box
    answer_input.delete(0, END)
    random_state() 

# Create state flashcard function
def states():
    hide_all_frames()
    state_frame.pack(fill=BOTH, expand=True)
    my_label = Label(state_frame, text="Something").pack()

    '''
    #Create a list of state names
    global our_states
    our_states = ['california', 'florida', 'illinois', 'kentucky', 'texas', 'hawaii'] #1 means california, 2 means florida etc

    #Generate a random number
    global rando
    rando = randint(0, len(our_states)-1)
    state = "img/flashcard/" + our_states[rando] + '.png' 

    #Creat state image 
    global state_image 
    state_image = ImageTk.PhotoImage(Image.open(state)) 
    '''
    global show_state
    show_state = Label(state_frame)
    show_state.pack(pady=15) 
    

    # Create answer input box
    global answer_input
    answer_input = Entry(state_frame, font="Helvetica 18")
    answer_input.pack(pady=15)

    #Create btn to randomize state images
    rando_button = Button(state_frame, text="Pass", command=states)
    rando_button.pack(pady=10)

    #Create a button to answer the question
    answer_button = Button(state_frame, text='Answer', command=state_answer)
    answer_button.pack(pady=5)

    #Create a label to tell us if answer right or not
    global answer_label
    answer_label = Label(state_frame, text="", font="Helvetica 18")
    answer_label.pack(pady=15) 
    
    


def state_capitals():
    hide_all_frames()
    state_capitals_frame.pack(fill=BOTH, expand=True)
    my_label = Label(state_capitals_frame, text="Something in state capital").pack()
    

# Hide all previous frames
def hide_all_frames():
    for widget in state_frame.winfo_children():
        widget.destroy()

    for widget in state_capitals_frame.winfo_children():
        widget.destroy()

    state_frame.pack_forget()
    state_capitals_frame.pack_forget()


my_menu = Menu(root)
root.config(menu=my_menu)

# Create menu items
states_menu = Menu(my_menu)
my_menu.add_cascade(label="Geography", menu=states_menu)
states_menu.add_command(label="States", command=states)
states_menu.add_command(label="State Capitals", command=state_capitals) 
states_menu.add_separator()
states_menu.add_command(label="Exit", command=root.quit)

# Create our frames
state_frame = Frame(root, width=500, height=500)
state_capitals_frame = Frame(root, width=500, height=500) 

root.mainloop()