from tkinter import * 

root = Tk()
root.title('Tkinter GUI - Sailendra')
root.geometry('400x400')

# Create a function that calculate matrix and display in new window
def calculate():
    window = Toplevel() 

    n1 = matrix_entry1
    n2 = matrix_entry2 # n2 and n3 should be same number
    n4 = matrix_entry4
    





# Create frame for heading, body and button
heading_frame = Frame(root)
heading_frame.grid(row=0, column=0, pady=10)

body_frame = Frame(root)
body_frame.grid(row=1, column=0, pady=10)

button_frame = Frame(root)
button_frame.grid(row=2, column=0, pady=10) 

# Creating a heading
heading_label = Label(heading_frame, text="Matrix Multiplier!!")
heading_label.pack()

#Create body content: two matrix Label field
matrix_label1 = Label(body_frame, text="Matrix A")
matrix_label1.grid(row=0, column=0)

matrix_label2 = Label(body_frame, text="Matrix B")
matrix_label2.grid(row=0, column=1)

#Create body content: two matrix entry field
matrix_entry1 = Entry(body_frame)
matrix_entry1.grid(row=1, column=0)
matrix_entry2 = Entry(body_frame)
matrix_entry2.grid(row=1, column=1)

matrix_entry3 = Entry(body_frame) 
matrix_entry3.grid(row=1, column=2)
matrix_entry4 = Entry(body_frame) 
matrix_entry4.grid(row=1, column=3)

# Create Button to calculate matrix
calculate_button = Button(button_frame, text="Calculate", command=calculate)
calculate_button.pack() 


root.mainloop()