from tkinter import *
from PIL import Image
from PIL.ImageTk import PhotoImage
from tkinter.messagebox import showerror

root = Tk()
root.title('Celsius to Fahrenheit - Sailendra')
root.geometry('700x500')
root.configure(bg="#F0C987")

#Create a function convert the temperature
def celsius_farenheit():
    try:
        user_input_celsius = int(value_entry.get())
        farenheit = (user_input_celsius * 9/5) + 32
        output_label.config(text=f"{user_input_celsius} is equal to {farenheit} farenheit.")

    except:
        showerror("Input Value Error", "Strings and Punctuation are not allowed!!")

    value_entry.delete(0, END)    


# Create frames
frame_heading = Frame(root, bg="#F0C987")
frame_heading.pack(pady=10)

frame_body = Frame(root, bg="#F0C987")
frame_body.pack(pady=10)

frame_output = Frame(root, bg="#F0C987")
frame_output.pack(pady=10)

frame_footer = Frame(root, bg="#F0C987") 
frame_footer.pack(pady=10) 

# Create heading label
heading_label = Label(frame_heading, text="Celsius to Fahrenheit", font="Courier 35 bold", bg="#F0C987", fg="#8B1E3F")
heading_label.pack(pady=10) 

#Create Entry field, formula label and answer button in body frame
global value_entry
value_entry = Entry(frame_body, width=10, bd=2, bg="#F0C987", font="courier 30", justify=CENTER)
value_entry.grid(pady=10, row=0, column=0) 

formula_text_label = Label(frame_body, text="Formula: (0°C × 9/5) + 32 = 32°F", bg="#F0C987", fg="#2D3047")
formula_text_label.grid(row=1, column=0) 

global answer_button
answer_button = Button(frame_body, text='Calculate', command=celsius_farenheit, font="courier 20 bold", bg="#F0C987", fg="#8B1E3F")
answer_button.grid(pady=(60, 0), row=2, column=0) 


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