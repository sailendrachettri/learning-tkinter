from tkinter import * 
import numpy as np
import matplotlib.pyplot as plt

root = Tk()
root.title('Tkinter GUI - Sailendra')
root.geometry('400x400')

def graph():
    house_prices = np.random.normal(2000000, 25000, 5000)
    plt.polar(house_prices)

    plt.show() 


my_button =Button(root, text="Show Graph", command=graph)
my_button.pack() 

root.mainloop()