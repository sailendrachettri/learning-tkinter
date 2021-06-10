from tkinter import *
from random import randint

root = Tk()
root.title('Tkinter GUI - Sailendra')
root.geometry('400x400')

def pick():
    entries = ['name 1', 'name 1', 'name 2', 'name 2', 'name 3', 'name 4', 'name 5', 'name 6', 'name 7', 'name 8', 'name 9', 'name 10', 'name 11', 'name 12', 'name 13', 'name 14', 'name 15', 'name 16', 'name 17', 'name 18', 'name 19', 'name 20']
    
    #Filterling duplicates
    entries_set = set(entries)
    unique_entries = list(entries_set)

    #create list size variable
    our_numbers = len(unique_entries) - 1
    #create random number in between 0 to our_numbers 
    rando = randint(0, our_numbers) 


    winner_label = Label(root, text=unique_entries[rando], font="Helvetica 24") 
    winner_label.pack(pady=50)

topLabel = Label(root, text="Win-O-Rama!", font="Helvetica 24")
topLabel.pack(pady=20)

winButton = Button(root, text="Pick our winner", font="Helvetica 24", command=pick)  
winButton.pack(pady=20)

root.mainloop() 