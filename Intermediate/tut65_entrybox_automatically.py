from tkinter import * 

root = Tk()
root.title('Tkinter GUI - Sailendra')
root.geometry('900x500')

my_entries = []

def something():
    entry_list = ''
    for entries in my_entries:
        entry_list = entry_list + str(entries.get()) + '\n'
        my_label.config(text=entry_list)
    
    # print(my_entries[3].get())

# Bunch of entry box - one row and one column
# for x in range(5):
#     my_entry = Entry(root)
#     my_entry.grid(row=0, column=x, pady=20, padx=4) 
#     my_entries.append(my_entry) 

# Bunch of entry box - multiple row and multiple
for y in range(5):
    for x in range(5):
        my_entry = Entry(root)
        my_entry.grid(row=y, column=x, pady=20, padx=4) 
        my_entries.append(my_entry) 

my_button = Button(root, text="Click me!", command=something)
my_button.grid(row=6, column=0, pady=20)

my_label = Label(root, text='')
my_label.grid(row=7, column=0, pady=20) 

root.mainloop()