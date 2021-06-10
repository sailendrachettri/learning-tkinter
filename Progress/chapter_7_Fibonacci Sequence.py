from tkinter import *
from tkinter.messagebox import showerror

root = Tk()
root.title('Fibonacci Sequence - Sailendra')
root.geometry('600x440')
root.configure(bg="#2E86AB")

#Create a function to generate fibonacci Sequence
def fibonacci_sequence():
    try:
        up_to = int(value_entry.get())
        n1, n2 = 0, 1
        count = 0

        val_list = []

        if up_to <= 0:
            showerror("Input Value Error", "Please Enter Valid number !!")
               
        elif up_to == 1:
            output_label.config(text="0")
            
        else:
            while count < up_to:
                val_list.append(n1)
                nth = n1 + n2

                n1 = n2
                n2 = nth
                count += 1

            output_label.config(text=val_list)

        value_entry.delete(0, END)

    except:
        showerror("Input Value Error", "Please Enter Valid number !!")
        


# Create frames
frame_heading = Frame(root, bg="#2E86AB")
frame_heading.pack(pady=10)

frame_body = Frame(root, bg="#2E86AB")
frame_body.pack(pady=10)

frame_output = Frame(root, bg="#2E86AB")
frame_output.pack(pady=10)


# Create heading label
heading_label = Label(frame_heading, text="Fibonacci Sequence", font="Courier 35 bold", bg="#2E86AB", fg="#EEEEFF")
heading_label.pack(pady=10) 
 
#Create Entry widget
global value_entry
value_entry = Entry(frame_body, font=("Times New Roman", "30","bold"), width=15, fg="#1F363D", justify=CENTER)
value_entry.grid(row=0, column=0)

# Create buttons
button = Button(frame_body, text="Find Now!", font="Helvetica 20", fg="#EEEEFF", bg="#2E86AB", command=fibonacci_sequence)
button.grid(row=1, column=0,pady=30, padx=15)


# Create a label for output
global output_label
output_label = Label(frame_output, text="", font="Courier 20 bold", fg="#EEEEFF", bg="#2E86AB")
output_label.pack() 

root.mainloop()