from tkinter import * 
import pygame

root = Tk()
root.title('Tkinter GUI - Sailendra')
root.geometry('400x400')

pygame.mixer.init() 

def play():
    pygame.mixer.music.load("songs/song.ogg") 
    pygame.mixer.music.play(loops=0)


my_button = Button(root, text="Play Song", command=play, font="Courier 20") 
my_button.pack(pady=20) 


root.mainloop() 