from tkinter import * 
import pyttsx3

root = Tk()
root.title('Tkinter GUI - Sailendra')
root.geometry('400x400')

def talk():
    engine = pyttsx3.init()

    #Properties

    engine.setProperty('rate', 150)
    voices = engine.getProperty('voices')
    engine.setProperty('voice', voices[2].id)

    engine.say(my_entry.get())
    engine.runAndWait() 

    my_entry.delete(0, END)

my_entry = Entry(root, font="Courier 20 bold")
my_entry.pack(pady=20)

my_button = Button(root, text="Speak", command=talk)
my_button.pack(pady=20)


root.mainloop()