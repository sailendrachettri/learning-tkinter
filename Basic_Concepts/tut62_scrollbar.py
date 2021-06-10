from tkinter import * 

root = Tk()
root.title('Tkinter GUI - Sailendra')
root.geometry('400x400')

# Create frame and scrollbar
my_frame = Frame(root)
my_scrollbar = Scrollbar(my_frame, orient=VERTICAL) 



# Creating List Box
#selectmode = SINGLE, MULTIPLE, BROWSE, EXTENDED
my_listbox = Listbox(my_frame, width=50, yscrollcommand=my_scrollbar.set, selectmode=MULTIPLE)

#Configure scrollbae
my_scrollbar.config(command=my_listbox.yview)
my_scrollbar.pack(side=RIGHT, fill=Y)

my_listbox.pack(pady=20)
my_frame.pack()

#Add list of items
my_list = ['one', 'two', 'three', 'four', 'one', 'two', 'three', 'four', 'one', 'two', 'three', 'four', 'one', 'two', 'three', 'four', 'one', 'two', 'three', 'four','one', 'two', 'three', 'four','one', 'two', 'three', 'four','one', 'two', 'three', 'four']

for item in my_list:
    my_listbox.insert(END, item)


def delete():
    my_listbox.delete(ANCHOR)
    my_label.config(text='item deleted!')

def select():
    my_label.config(text=my_listbox.get(ANCHOR))

def delete_all():
    my_listbox.delete(0, END)

def select_all():
    result = ''

    for item in my_listbox.curselection():
        result = result + str(my_listbox.get(item)) + '\n'

    my_label.config(text=result)

def delete_multiple():
    for item in reversed(my_listbox.curselection()):
        my_listbox.delete(item)
    


my_button = Button(root, text="Delete", command=delete)
my_button.pack()

my_button2 = Button(root, text="Select", command=select)
my_button2.pack()

my_button3 = Button(root, text="Delete All", command=delete_all)
my_button3.pack()

my_button4 = Button(root, text="Select All", command=select_all)
my_button4.pack()

my_button5 = Button(root, text="Delete multiple", command=delete_multiple)
my_button5.pack()

global my_label
my_label = Label(root, text='')
my_label.pack(pady=10)

root.mainloop()   