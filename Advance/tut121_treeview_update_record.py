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
tree_frame.pack(pady=10)

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
add_frame.pack(pady=10) 

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

# Select record
def select_record():
    # Clear entry boxes
    name_box.delete(0, END)
    id_box.delete(0, END)
    topping_box.delete(0, END)

    # Grab record number
    selected = my_tree.focus()

    # Grab record values
    values = my_tree.item(selected, 'values')  
    # temp_label.config(text=values[0])
    # print(values)

    #Output to entry boxes 
    name_box.insert(0, values[0])
    id_box.insert(0, values[1])
    topping_box.insert(0, values[2])
    

# Save update record
def update_record():
    # Grab record number
    selected = my_tree.focus() 

    # Save new data
    my_tree.item(selected, text="", values=(name_box.get(), id_box.get(), topping_box.get()))

    # Clear entry boxes
    name_box.delete(0, END)
    id_box.delete(0, END)
    topping_box.delete(0, END)

# Create binding click function
def clicker(e):
    select_record()

#Move up row
def moves_up():
    rows = my_tree.selection()
    for row in rows:
        my_tree.move(row, my_tree.parent(row), my_tree.index(row)-1) 

def moves_down():
    rows = my_tree.selection()
    for row in reversed(rows):
        my_tree.move(row, my_tree.parent(row), my_tree.index(row)+1) 

#Buttons 
move_up = Button(root, text="Move up", command=moves_up)
move_up.pack(pady=5)

moves_down = Button(root, text="Move Down", command=moves_down)
moves_down.pack(pady=5)

select_button = Button(root, text="Select Record", command=select_record)
select_button.pack(pady=10)

update_button = Button(root, text="Update Record", command=update_record)
update_button.pack(pady=10)

add_record = Button(root, text="Add record", command=add_record)
add_record.pack(pady=10)

#Remove all records
remove_record_all= Button(root, text="Romove all Records", command=remove_all) 
remove_record_all.pack(pady=10)

#Remove one record selected
remove_one_record = Button(root, text="Remove one", command=remove_one)
remove_one_record.pack(pady=10)

#Remove many records selected
remove_many_record = Button(root, text="Remove many", command=remove_many)
remove_many_record.pack(pady=10)

temp_label = Label(root, text="")
temp_label.pack(pady=10)

# Binding
# my_tree.bind("<Double-1>", clicker)
my_tree.bind("<ButtonRelease-1>", clicker)

root.mainloop()