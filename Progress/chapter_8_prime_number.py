from tkinter import *
from tkinter.messagebox import showerror

root = Tk()
root.title('Prime Number - Sailendra')
root.geometry('600x440')
root.configure(bg="#2E86AB")

#Create a function to generate Prime Number
def prime_numbers():
    try:
        val = int(value_entry.get())
        val_list = []

        for num in range(2, val+1):
            if num > 1:
                for i in range(2, num):
                    if (num % i) == 0:
                        break
                else:
                    val_list.append(num)
    
        output_label.config(text=val_list)  
    except:
        showerror("Invalid Input", "Please enter a valid number!!")

    value_entry.delete(0,END)
        


# Create frames
frame_heading = Frame(root, bg="#2E86AB")
frame_heading.pack(pady=10)

frame_body = Frame(root, bg="#2E86AB")
frame_body.pack(pady=10)

frame_output = Frame(root, bg="#2E86AB")
frame_output.pack(pady=10)


# Create heading label
heading_label = Label(frame_heading, text="Prime Numbers", font="Courier 35 bold", bg="#2E86AB", fg="#EEEEFF")
heading_label.pack(pady=10) 

 
#Create Entry widget
global value_entry
value_entry = Entry(frame_body, font=("Times New Roman", "30","bold"), width=15, fg="#1F363D", justify=CENTER)
value_entry.grid(row=0, column=0)

#Create help text underneath Entry widgets 
help_text_label = Label(frame_body, text="Prime number till n", bg="#2E86AB", font="Courier 17")
help_text_label.grid(row=1, column=0, pady=5)

# Create buttons
button = Button(frame_body, text="Generate", font="Helvetica 20", fg="#EEEEFF", bg="#2E86AB", command=prime_numbers)
button.grid(row=2, column=0,pady=30, padx=15)


# Create a label for output
global output_label
output_label = Label(frame_output, text="", font="Courier 20 bold", fg="#EEEEFF", bg="#2E86AB")
output_label.pack() 

root.mainloop()