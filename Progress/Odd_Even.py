from tkinter import *

root = Tk()
root.title('Tkinter GUI - Sailendra')
root.geometry('436x400')
root.configure(background="powder blue")  

display_number = Label(root)

# Create a function to peform operations and display value
def check_number():

    global display_number
    display_number.destroy()

    if(entry_number.get().isdigit()):
        user_input = int(entry_number.get())

        if (user_input %2 == 0):
            display_number = Label(output_frame, text= str(user_input) + " is Even Number.\n", font="Courier 15", bg="powder blue")
            display_number.grid(row=1, column=0, pady=(25, 0))

        else:
            display_number = Label(output_frame, text=str(user_input) + " is Odd Number.\n", font="Courier 15", bg="powder blue")
            display_number.grid(row=2, column=0, pady=(25, 0))
    else:
        display_number = Label(output_frame, text=str(entry_number.get()) + " is Invalid.\n", font="Courier 15", bg="powder blue")
        display_number.grid(row=2, column=0, pady=(25, 0))



# Frames to seperate the content
heading_frame = Frame(root, borderwidth=1, relief=SUNKEN, padx=10, pady=5, bg="powder blue")
heading_frame.grid(row=0, column=0, ipadx=50, pady=8, padx=10) 

content_frame = Frame(root, borderwidth=1, relief=SUNKEN, padx=10, pady=10, bg="powder blue")
content_frame.grid(row=1, column=0, pady=20)

button_frame = Frame(root, borderwidth=1, relief=SUNKEN, padx=10, pady=10, bg="powder blue")
button_frame.grid(row=2, column=0, pady=20) 

output_frame = Frame(root, borderwidth=1, relief=SUNKEN, padx=10, bg="powder blue")
output_frame.grid(row=3, column=0, pady=20) 

#Create a label for heading
heading_label = Label(heading_frame, text="Odd or Even", font=("times new roman", "26", "bold"), bg="powder blue")
heading_label.grid(padx=(100, 0))

#Create a label for entry widget
entry_label = Label(content_frame, text="Enter Number: ", font="Courier 20", bg="powder blue")
entry_label.grid(row=1, column=0) 

#Create Input box to enter number
entry_number = Entry(content_frame, font="Courier 20", width=10)
entry_number.grid(row=1, column=1)

#Create display button
display_button = Button(button_frame, text="Check", command=check_number, font="Courier 20 bold", bg='powder blue')
display_button.grid(row=0, column=0, pady=10)

root.mainloop()


