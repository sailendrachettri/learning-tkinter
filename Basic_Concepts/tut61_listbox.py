from tkinter import * 

root = Tk()
root.title('Tkinter GUI - Sailendra')
root.geometry('400x400')

# Creating List Box
my_listbox = Listbox(root)
my_listbox.pack(pady=20)

#Add item to listbox
# my_listbox.insert(END, "Item one")
# my_listbox.insert(END, "Item two") 

#Add list of items
my_list = ['one', 'two', 'three', 'four']

for item in my_list:
    my_listbox.insert(END, item)

my_listbox.insert(2, 'item') # here 2 is the position

def delete():
    my_listbox.delete(ANCHOR)
    my_label.config(text='item deleted!')

def select():
    my_label.config(text=my_listbox.get(ANCHOR))

my_button = Button(root, text="Delete", command=delete)
my_button.pack()

my_button2 = Button(root, text="Select", command=select)
my_button2.pack()

global my_label
my_label = Label(root, text='')
my_label.pack(pady=10)

root.mainloop()   