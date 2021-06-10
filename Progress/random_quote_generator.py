from tkinter import *  
from random import randint
from PIL import Image, ImageTk



root = Tk()
root.title('Random Quotes Generator - Sailendra')
root.geometry('1357x900')
root.configure(background='#20bd8e')

# Writing Label for heading 
heading_label = Label(root, text="Random Quotes Generator", font="courier 40 bold", anchor='center', bg='#20bd8e')
heading_label.pack(pady=55) 

# Creating a list of quotes
quotes_list = ["“First, solve the problem. Then, write the code.”",\
                "“Any fool can write code that a computer can understand. \nGood programmers write code that humans can understand.”",
                "“Experience is the name everyone gives to their mistakes.”",
                "“ In order to be irreplaceable, one must always be different”",
                "“Java is to JavaScript what car is to Carpet.”",
                "“Knowledge is power.”",
                "“Sometimes it pays to stay in bed on Monday, rather than spending \nthe rest of the week debugging Monday’s code.”",
                "“Perfection is achieved not when there is nothing more to add, \nbut rather when there is nothing more to take away.”",
                "“Ruby is rubbish! PHP is phpantastic!”",
                "“ Code is like humor. When you have to explain it, it’s bad.”",
                "“Fix the cause, not the symptom.”",
                "“Simplicity is the soul of efficiency.”",
                "“Before software can be reusable it first has to be usable.”",
                "“Make it work, make it right, make it fast.”",
                "“ Dont't worry if it doesn't work right.\nIf everything did, you'd be out of a job.”",
                "“ Don't comment bad code - rewrite it.”",
                "“One of my most productive days was throwing away 1000 lines of code.”",
                "“One main'scrappy software is another man's full time job.”",
                "“System programmers are the high priests of a low cult.”",
                "“The computer was born to solve problems that did not exist before.”",
                "“ People don't care about what you say, they care about what you build.”",
                "“We have to stop optimizing for programmers and start optimizing for users.”",
                "“We have to stop optimizing for programmers and start optimizing for users.”",
                "“ If you optimize everything, you will always be unhappy.”",
                "“Talk is cheap.Show me the code.”",
                "“Your most unhappy customers are your greatest source of learning.”",
                "“Developer is an organism that turns coffee into code.”",
                "“The purpose of software engineering is to control complexity, not to create it.”",
                "“Testing can only prove the presence of bugs, not their absence.”",
                "“Small minds are concerned with the extraordinary, great minds with the ordinary.”"
                ]

label_text = Label(root) 

#A function which is display quotes in root window 
def randon_quote_function():
    global label_text
    label_text.destroy()

    length_list = len(quotes_list) 
    randon_quote = randint(0, length_list) - 1 # minus one because list starts from zero

    label_text = Label(root, text=quotes_list[randon_quote], font='Georgia 20', bg='#20bd8e', fg='white')
    label_text.pack(pady=70) 


#Creating button to display quotes randomly
display_button = Button(root, text="Quotes", font="courier 20 bold", bg='orange', fg='white', command=randon_quote_function, anchor=CENTER)
display_button.pack()

#Add siganture of author
author_image = Image.open('/home/sailendrachettri/Learning /codes/Tkinter_CODEMY/img/sailendra.png')
resize_image = author_image.resize((150, 150), Image.ANTIALIAS)
img = ImageTk.PhotoImage(resize_image)
image_label = Label(image=img, anchor=W, bg='#20bd8e')
image_label.pack(side=BOTTOM, pady=(0, 50)) 

root.mainloop() 