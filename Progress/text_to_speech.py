from tkinter import *
import pyttsx3 
from tkinter.messagebox import showwarning
from PIL.ImageTk import PhotoImage
from PIL import Image

root = Tk()
root.title('Tkinter GUI - Sailendra')
root.geometry('700x400')
root.configure(bg='#f6fa19')

# Create a function to convert text to speech
def speak():
    engine = pyttsx3.init()

    # Checking if text box is empty or not
    txt = input_text.get()
    if txt == "":
        showwarning("Warning", "Please enter text !!")
    else:
        engine.say(txt) 
        engine.runAndWait() 

    input_text.delete(0, END)

# Create frames to seperate the content
heading_frame = Frame(root, bg="#f6fa19")
heading_frame.pack(pady=(30, 0))

content_frame = Frame(root, bg="#f6fa19")
content_frame.pack(pady=10)

footer_frame = Frame(root, bg="#f6fa19")
footer_frame.pack(pady=10)

# Create heading label text
heading = Label(heading_frame, text="Text to Speech", font="Courier 35 bold", bg="#f6fa19") 
heading.pack()

#Create a entry widget to take text as input
input_text = Entry(content_frame, font="Helvetica 20 bold", bg="#f6fa19", width=30, bd=5, relief=RIDGE)
input_text.grid(row=1, column=0, pady=20)

#Create a button to call a function
button = Button(content_frame, text="Speak Now!", command=speak, font="courier 20 bold")
button.grid(row=2, column=0) 

#Footer image/text
image = Image.open('img/sailendra.png')
resized = image.resize((160, 80), Image.ANTIALIAS)
new_image = PhotoImage(resized)
footer_image = Label(footer_frame, image=new_image, bg="#f6fa19")
footer_image.pack(pady=(60, 0)) 


root.mainloop()