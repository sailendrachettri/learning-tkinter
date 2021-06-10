from tkinter import * 
from tkinter import ttk

root = Tk()
root.title('Tkinter GUI - Sailendra')
root.geometry('700x700')

#Add style
style = ttk.Style()

#Pick a theme
style.theme_use("alt") # default, clam, alt

# Create treeview frame
tree_frame = Frame(root)
tree_frame.pack(pady=20)

# Create treeview scrollbar
tree_scroll = Scrollbar(tree_frame)
tree_scroll.pack(side=RIGHT, fill=Y)

# Create tree view
my_tree = ttk.Treeview(tree_frame, yscrollcommand=tree_scroll.set, selectmode=EXTENDED) # selectmode = EXTENDED, NONE, BROWSE
my_tree.pack() 

# Configure the scrollbar
tree_scroll.config(command=my_tree.yview) 

# Define columns
my_tree['columns'] = ("Name", "ID", "Favourite Piaaz") 

#Fromate columns
my_tree.column("#0", width=0, stretch=NO) #width = 120, minwidth=25
my_tree.column("Name", anchor=W, width=140)
my_tree.column("ID", anchor=CENTER, width=100)
my_tree.column("Favourite Piaaz", anchor=W, width=140)

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

# Create striped row tags
my_tree.tag_configure('oddrow', background="white")
my_tree.tag_configure('evenrow', background="lightblue") 

global count
count = 0

for record in data:
    if count %2 == 0:
        my_tree.insert(parent='', index='end', iid=count, text="", values=(record[0], record[1], record[2]), tags=('evenrow',))
    else:
        my_tree.insert(parent='', index='end', iid=count, text="", values=(record[0], record[1], record[2]), tags=('oddrow',))

    count += 1

# Create frame(s)
add_frame = Frame(root)
add_frame.pack(pady=20) 

# Create labels
nl = Label(add_frame, text="Name")
nl.grid(row=0, column=0)

il = Label(add_frame, text="ID")
il.grid(row=0, column=1)

tl = Label(add_frame, text="Topping")
tl.grid(row=0, column=2) 

# Entry boxes
name_box = Entry(add_frame)
name_box.grid(row=1, column=0) 

id_box = Entry(add_frame)
id_box.grid(row=1, column=1)

topping_box = Entry(add_frame)
topping_box.grid(row=1, column=2) 

# Add record function
def add_record():
    global count
    if count %2 == 0:
        my_tree.insert(parent='', index='end', iid=count, text="", values=(name_box.get(), id_box.get(), topping_box.get()), tags=('evenrow',))
    else:
        my_tree.insert(parent='', index='end', iid=count, text="", values=(name_box.get(), id_box.get(), topping_box.get()), tags=('oddrow',))
    
    count += 1

    # clear boxes
    name_box.delete(0, END)
    id_box.delete(0, END)
    topping_box.delete(0, END)

# Remove all record function
def remove_all():
    for record in my_tree.get_children():
        my_tree.delete(record) 

# Remove one selected record function
def remove_one():
    x = my_tree.selection()[0]
    my_tree.delete(x)

# Remove many selected records
def remove_many():
    x = my_tree.selection()
    for record in x:
        my_tree.delete(record)


#Buttons 
add_record = Button(root, text="Add record", command=add_record)
add_record.pack(pady=20)

#Remove all records
remove_record_all= Button(root, text="Romove all Records", command=remove_all) 
remove_record_all.pack(pady=10)

#Remove one record selected
remove_one_record = Button(root, text="Remove one", command=remove_one)
remove_one_record.pack(pady=10)

#Remove many records selected
remove_many_record = Button(root, text="Remove many", command=remove_many)
remove_many_record.pack(pady=10)



root.mainloop()