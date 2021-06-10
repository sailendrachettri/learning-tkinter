from tkinter import *
from PIL import Image
from PIL.ImageTk import PhotoImage
from tkinter.messagebox import showerror

root = Tk()
root.title('Greater Number - Sailendra')
root.geometry('700x500')
root.configure(bg="#F0C987")

#Create a function to check which number greator
def greater_number():
    try:
        val1 = int(value_entry1.get())
        val2 = int(value_entry2.get())

        if val1 > val2:
            output_label.config(text=f"{val1} is Greater.")

        elif val1 == val2:
            output_label.config(text=f"{val1} and {val2} both are same.")
        
        else:
            output_label.config(text=f"{val2} is Greater.")

    except:
        showerror("Input value error", "Only Integer numbers are allowed !!")

    # Clearing the input field
    value_entry1.delete(0, END)
    value_entry2.delete(0, END)

# Create frames
frame_heading = Frame(root, bg="#F0C987")
frame_heading.pack(pady=10)

frame_body = Frame(root, bg="#F0C987")
frame_body.pack(pady=10)

frame_button = Frame(root, bg="#F0C987") 
frame_button.pack(pady=10) 

frame_output = Frame(root, bg="#F0C987")
frame_output.pack(pady=10)

frame_footer = Frame(root, bg="#F0C987") 
frame_footer.pack(pady=10) 

# Create heading label
heading_label = Label(frame_heading, text="Greater Number", font="Courier 35 bold", bg="#F0C987", fg="#8B1E3F")
heading_label.pack(pady=10) 

#Create two Entry field
global value_entry1
value_entry1 = Entry(frame_body, width=10, bd=2, bg="#F0C987", font="courier 30", justify=CENTER)
value_entry1.grid(pady=10, padx=5, row=0, column=0) 

global value_entry2
value_entry2 = Entry(frame_body, width=10, bd=2, bg="#F0C987", font="courier 30", justify=CENTER)
value_entry2.grid(pady=10, row=0, column=1) 

# Create two label field for entry widgit one and two
help_text_label = Label(frame_body, text="Enter number 1", bg="#F0C987", fg="#2D3047")
help_text_label.grid(row=1, column=0) 

help_text_label = Label(frame_body, text="Enter number 2", bg="#F0C987", fg="#2D3047")
help_text_label.grid(row=1, column=1) 

# Create a Button
global answer_button
answer_button = Button(frame_button, text='Check', command=greater_number, font="courier 20 bold", bg="#F0C987", fg="#8B1E3F")
answer_button.pack(pady=20) 


# Create a label for output
global output_label
output_label = Label(frame_output, text="", font="Courier 20 bold", fg="#8B1E3F", bg="#F0C987")
output_label.pack() 

# Create a Label for footer image
image = Image.open('img/sailendra.png')
resized = image.resize((160, 80), Image.ANTIALIAS)
final_image = PhotoImage(image=resized)
image_label  = Label(frame_footer, image=final_image, bg="#F0C987")
image_label.pack(pady=(60, 0)) 


root.mainloop()