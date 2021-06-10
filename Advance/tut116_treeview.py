from tkinter import * 
from tkinter import ttk

root = Tk()
root.title('Tkinter GUI - Sailendra')
root.geometry('400x400')

my_tree = ttk.Treeview(root) 

# Define columns
my_tree['columns'] = ("Name", "ID", "Favourite Piaaz") 

#Fromate columns
my_tree.column("#0", width=0, stretch=NO) #width = 120, minwidth=25
my_tree.column("Name", anchor=W, width=120)
my_tree.column("ID", anchor=CENTER, width=80)
my_tree.column("Favourite Piaaz", anchor=W, width=120)

# Create heading - treeview
my_tree.heading("#0", text="", anchor=W) # text="Label"
my_tree.heading("Name", text="Name", anchor=W)
my_tree.heading("ID", text="ID", anchor=CENTER)
my_tree.heading("Favourite Piaaz", text="Favourite Piaaz", anchor=W)

# Add data - what if rows are in million - or fetching from database
data = [
        ["John", 1, "Peperroine"],
        ["Sai", 2, "Banana"],
        ["Len", 3, "Mango"],
        ["Dra", 4, "Orange"],
        ["Sailendra", 5, "Apple"],
        ["Pravesh", 6, "Litche"],
        ["Youraj", 7, "Omegal"],
        ["Raju", 8, "No omegal"],
        ["Rahul", 9, "Santaclus"],
        ["Rohi", 10, "Rangom data"],
        ["Rakesh", 11, "Boring stuff"],
]

count = 0
for record in data:
    my_tree.insert(parent='', index='end', iid=count, text="", values=(record[0], record[1], record[2]))
    count += 1
    
"""
# Add data -  without the initial label
my_tree.insert(parent='', index='end', iid=0, text="", values=("John", 1, "Peperroine"))
my_tree.insert(parent='', index='end', iid=1, text="", values=("Sai", 2, "Banana"))
my_tree.insert(parent='', index='end', iid=2, text="", values=("Len", 3, "Mango"))
my_tree.insert(parent='', index='end', iid=3, text="", values=("Dra", 4, "Orange"))
my_tree.insert(parent='', index='end', iid=4, text="", values=("Sailendra", 5, "Apple"))
my_tree.insert(parent='', index='end', iid=5, text="", values=("Pravesh", 6, "Litche"))
my_tree.insert(parent='', index='end', iid=6, text="", values=("Youraj", 7, "Omegal"))
my_tree.insert(parent='', index='end', iid=7, text="", values=("Raju", 8, "No omegal"))
my_tree.insert(parent='', index='end', iid=8, text="", values=("Rahul", 9, "Santaclus"))
my_tree.insert(parent='', index='end', iid=9, text="", values=("Rohi", 10, "Rangom data"))
my_tree.insert(parent='', index='end', iid=10, text="", values=("Rakesh", 11, "Boring stuff"))


# Add data - boring stuff
my_tree.insert(parent='', index='end', iid=0, text="Parent", values=("John", 1, "Peperroine"))
my_tree.insert(parent='', index='end', iid=1, text="Parent", values=("Sai", 2, "Banana"))
my_tree.insert(parent='', index='end', iid=2, text="Parent", values=("Len", 3, "Mango"))
my_tree.insert(parent='', index='end', iid=3, text="Parent", values=("Dra", 4, "Orange"))
my_tree.insert(parent='', index='end', iid=4, text="Parent", values=("Sailendra", 5, "Apple"))
my_tree.insert(parent='', index='end', iid=5, text="Parent", values=("Pravesh", 6, "Litche"))
my_tree.insert(parent='', index='end', iid=6, text="Parent", values=("Youraj", 7, "Omegal"))
my_tree.insert(parent='', index='end', iid=7, text="Parent", values=("Raju", 8, "No omegal"))
my_tree.insert(parent='', index='end', iid=8, text="Parent", values=("Rahul", 9, "Santaclus"))
my_tree.insert(parent='', index='end', iid=9, text="Parent", values=("Rohi", 10, "Rangom data"))
my_tree.insert(parent='', index='end', iid=10, text="Parent", values=("Rakesh", 11, "Boring stuff"))

# Add child data
my_tree.insert(parent='0', index='end', iid=11, text="Child", values=("Steve", 1.1, "Peppers"))
# my_tree.move('11', '0', '0') # give parent = id_num or wrote this line and move to the child section
"""

# Finally, pach this widgets
my_tree.pack(pady=20)


root.mainloop()