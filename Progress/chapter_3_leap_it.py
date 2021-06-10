from tkinter import *
from PIL import Image
from PIL.ImageTk import PhotoImage
from tkinter.messagebox import showerror

root = Tk()
root.title('Greater Number - Yourname')
root.geometry('700x500')
root.configure(bg="#28587B")

# Create a function to check whether a year is function or not
def leap_it_function():
    try:
        year = int(value_entry.get())
        if (year % 400 == 0 and year % 100 != 0) or year % 4 == 0:
            output_label.config(text=f"{year} is leap year.")
        
        else:
            output_label.config(text=f"{year} is not leap year.")

    except:
        showerror("Input value error", "Only Integer value are allowed!")

    value_entry.delete(0, END)
    

# Create frames for heading, body, and output
frame_heading = Frame(root, bg="#28587B")
frame_heading.pack(pady=10)

frame_body = Frame(root, bg="#28587B")
frame_body.pack(pady=10)

frame_output = Frame(root, bg="#28587B")
frame_output.pack(pady=(60, 0))


# Create heading label
heading_label = Label(frame_heading, text="Leap Year", font="Courier 35 bold", bg="#28587B", fg="#EEEEFF")
heading_label.pack(pady=10) 
 
# Create a entry widget, a help text and a button inside the body frame
global value_entry
value_entry = Entry(frame_body, width=10, bd=2, bg="#28587B", fg="#EEEEFF", font="courier 30", justify=CENTER)
value_entry.grid(pady=10, row=0, column=0)

help_text_label = Label(frame_body, text="Enter a year, example: 2021", bg="#28587B", fg="#EEEEFF")
help_text_label.grid(row=1, column=0) 

answer_button = Button(frame_body, text='Check', command=leap_it_function, font="courier 20 bold", bg="#28587B", fg="#EEEEFF")
answer_button.grid(pady=(60, 0), row=2, column=0) 

# Create a label for output
global output_label
output_label = Label(frame_output, text="", font="Courier 20 bold", fg="#EEEEFF", bg="#28587B")
output_label.pack() 

root.mainloop()