from tkinter import *
from PIL import Image
from PIL.ImageTk import PhotoImage


root = Tk()
root.title('Guessing Game - Sailendra')
root.geometry('600x400')
root.configure(background='#fcba03')

label_output = Label(root)

def show_number():

    # Clearing previous output from screen
    global label_output
    label_output.destroy() 

    my_number = 8

    # Check if input is number or string
    if entry_number.get().isdigit():
        #Converting string to integer
        user_number = int(entry_number.get())

        # Create a label to display result and validate number
        if(user_number < my_number):
            label_output = Label(frame_output, text="Oops! try little big number", font="Courier 20 bold", bg='#fcba03')
            label_output.pack(pady=(30, 5))
        
        elif (user_number == my_number):
            label_output = Label(frame_output, text="Great! you won !!", font="Courier 20 bold", bg='#fcba03')
            label_output.pack(pady=(30, 5))

        else:
            label_output = Label(frame_output, text="Oops! try little small number", font="Courier 20 bold", bg='#fcba03')
            label_output.pack(pady=(30, 5))

    else:
        label_output = Label(frame_output, text="Sorry! allow number only!", font="Courier 20 bold", bg='#fcba03')
        label_output.pack(pady=(30, 5))


# Create frames for heading, main body and output
frame_heading = Frame(root, pady=10, bg='#fcba03')
frame_heading.pack(pady=20)

frame_body = Frame(root, bg='#fcba03')
frame_body.pack()

frame_output = Frame(root, bg='#fcba03')
frame_output.pack()

frame_footer = Frame(root, bg='#fcba03')
frame_footer.pack(side=BOTTOM)

# Create heading label text
label_heading = Label(frame_heading, text="Guess the Number", font="Courier 30 bold", bg='#fcba03')
label_heading.pack()

# Body content: Create Entry field to input number
entry_number = Entry(frame_body, bg='#03fc07', font='Helvetica 26 bold', width=10, justify=CENTER)
entry_number.grid(row=0, column=0)

entry_text = Label(frame_body, text="Enter between 0 to 10", bg='#fcba03', font='bold')
entry_text.grid(row=1, column=0, pady=(3, 15))


# Body content: Create Button to display output
button_guess = Button(frame_body, text="Guess", command=show_number, font="Georgia, 23 bold")
button_guess.grid(row=2, column=0)

# Adding footer image signature
image_footer = Image.open("img/sailendra.png")
image_resize = image_footer.resize((120, 70), Image.ANTIALIAS)
img = PhotoImage(image_resize)

lbl = Label(frame_footer, image=img, bg='#fcba03', anchor=S)
lbl.pack(side=BOTTOM) 


root.mainloop()

