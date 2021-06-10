from tkinter import *
from math import sqrt
from tkinter.messagebox import showerror

root = Tk()
root.title('Quadratic Equation - Sailendra')
root.geometry('870x630')
root.configure(bg="#006D77")

#Create a function to solve quadratic equation
def quadratic_equaltion():
    try:
        # Getting value as a imput from user
        value_a = int(entry_a.get())
        value_b = int(entry_b.get()) 
        value_c = int(entry_c.get())

        # Calculating descriminant i.e (-b + b*b)/2a or (-b - b*b)/2a
        discriminant = (value_b * value_b) - (4 * value_a * value_c)

        dis_sqrt = sqrt(abs(discriminant)) # Finding square of discriminant

        # Finding two roots
        solution_one = round((-value_b + dis_sqrt)/ (2 * value_a), 4)
        solution_two = round((-value_b - dis_sqrt)/ (2 * value_a), 4)

        if discriminant > 0:
            ans_label.config(text=f"Roots are real and different i.e {solution_one} & {solution_two}.")

        elif discriminant == 0:
            ans_label.config(text=f"Roots are real and same i.e {solution_one} & {solution_two}.")

        else:
            ans_label.config(text=f"Roots are Imaginary i.e {solution_one} + i {solution_two}.")
    except:
        showerror("Invalid Input", "Invalid Input. Plese Try different values !!")

    entry_a.delete(0, END)
    entry_b.delete(0, END)
    entry_c.delete(0, END)

# Create heading frame
frame_heading = Frame(root, bg="#006D77")
frame_heading.pack(pady=10)

# Create main frame and back other frame in this main frame
frame_main = Frame(root, bg="#006D77", relief=RAISED, bd=2, padx=100, pady=40)
frame_main.pack(pady=20)

frame_body = Frame(frame_main, bg="#006D77")
frame_body.pack(pady=10)

frame_button = Frame(frame_main, bg="#006D77") 
frame_button.pack(pady=10) 

frame_output = Frame(frame_main, bg="#006D77")
frame_output.pack(pady=10)

# Create heading label
heading_label = Label(frame_heading, text="Quadratic Equation", font=("Times New Roman", "30", "bold"), fg="#EEEEFF",bg="#006D77")
heading_label.pack(pady=10) 

# Create three label text A, B, C
label_a = Label(frame_body, text="A", font=("Times New Roman", "26"), fg="#EEEEFF",bg="#006D77")
label_a.grid(row=0, column=0)

label_a = Label(frame_body, text="B", font=("Times New Roman", "26"), fg="#EEEEFF",bg="#006D77")
label_a.grid(row=0, column=1)

label_a = Label(frame_body, text="C", font=("Times New Roman", "26"), fg="#EEEEFF",bg="#006D77")
label_a.grid(row=0, column=2) 

# Create three entry box to enter three values
entry_a = Entry(frame_body, font=("Times New Roman", "30", "bold"), fg="#EEEEFF",bg="#006D77", width=7, justify=CENTER)
entry_a.grid(row=1, column=0, padx=5)

entry_b = Entry(frame_body, font=("Times New Roman", "30", "bold"), fg="#EEEEFF",bg="#006D77", width=7, justify=CENTER)
entry_b.grid(row=1, column=1, padx=5)

entry_c = Entry(frame_body, font=("Times New Roman", "30", "bold"), fg="#EEEEFF",bg="#006D77", width=7, justify=CENTER)
entry_c.grid(row=1, column=2, padx=5)

# Creat a button to submit call a function
solve_button = Button(frame_button, text="Solve", command=quadratic_equaltion, font=("Times New Roman", "22"), fg="#EEEEFF",bg="#006D77", width=29)
solve_button.pack(pady=10) 

# Create a label to display output on screen
ans_label = Label(frame_output, text="", font=("Times New Roman", "20"), fg="#EEEEFF", bg="#006D77")
ans_label.pack()

root.mainloop()