from tkinter import * 
from tkinter import ttk
import time

root = Tk()
root.title('Tkinter GUI - Sailendra')
root.geometry('400x400')

def step():
    my_progress['value'] += 10
    # my_progress.start(10)

    my_label.config(text=my_progress['value'])

    # for x in range(10):
    #     my_progress['value'] += 10
    #     root.update_idletasks() 
    #     time.sleep(1)
    
    # my_progress.stop() 

def stop():
    my_progress.stop()



my_progress = ttk.Progressbar(root, orient=HORIZONTAL, length=300, mode='determinate') # 'indeterminate'
my_progress.pack(pady=20)

my_button = Button(root, text="Start", command=step) 
my_button.pack(pady=20) 

my_button2 = Button(root, text="Stop", command=stop) 
my_button2.pack(pady=20) 

my_label = Label(root, text="")
my_label.pack(pady=20)
root.mainloop()