from tkinter import *

root = Tk()
root.title('Greater Number - Sailendra')
root.geometry('700x500')
root.configure(bg="#F0C987")

#Create a function

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
 


# Create a label for output
global output_label
output_label = Label(frame_output, text="", font="Courier 20 bold", fg="#8B1E3F", bg="#F0C987")
output_label.pack() 



root.mainloop()