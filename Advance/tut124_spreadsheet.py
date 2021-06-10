from tkinter import * 
from openpyxl.workbook import Workbook
from openpyxl import load_workbook

root = Tk()
root.title('Tkinter GUI - Sailendra')
root.geometry('400x400')

my_list = ["one", "two", "three"]

#Create listbox
my_listbox = Listbox(root, width=45)
my_listbox.pack(pady=20) 

# Create a work book
wb = load_workbook("/home/sailendrachettri/Learning /codes/Tkinter_CODEMY/Samples/excel.xlsx")

for item in my_list:
    my_listbox.insert(END, item) 

root.mainloop() 