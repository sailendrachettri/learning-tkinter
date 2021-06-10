from tkinter import * 
import sqlite3

root = Tk()
root.title('Tkinter GUI - Sailendra')


#function to update a record
def update():
    editor = Tk()
    editor.title("Update a Record")

    #Create and connect to database
    conn = sqlite3.connect('address_book.db')

    #create cursor
    c = conn.cursor()

    record_id = update_box.get()
    #update  a record
    c.execute(f"SELECT * FROM addresses WHERE oid= {record_id}")
    records = c.fetchall()

    #Creating text box
    f_name_editor = Entry(editor, width=30)
    f_name_editor.grid(row=0, column=1, padx=20, pady=(10, 0))

    l_name_editor = Entry(editor, width=30)
    l_name_editor.grid(row=1, column=1, padx=20) 

    address_editor = Entry(editor, width=30)
    address_editor.grid(row=2, column=1, padx=20) 

    city_editor = Entry(editor, width=30)
    city_editor.grid(row=3, column=1, padx=20) 

    state_editor = Entry(editor, width=30)
    state_editor.grid(row=4, column=1, padx=20) 

    zipcode_editor = Entry(editor, width=30)
    zipcode_editor.grid(row=5, column=1, padx=20) 


    #creating label for textbox
    f_name_label_editor = Label(editor, text="First Name: ", width=30, anchor=W)
    f_name_label_editor.grid(row=0, column=0, padx=20, pady=(10, 0)) 

    l_name_label_editor = Label(editor, text="Last Name: ", width=30, anchor=W)
    l_name_label_editor.grid(row=1, column=0, padx=20) 

    address_label_editor = Label(editor, text="Address: ", width=30, anchor=W)
    address_label_editor.grid(row=2, column=0, padx=20) 

    city_label_editor = Label(editor, text="City: ", width=30, anchor=W)
    city_label_editor.grid(row=3, column=0, padx=20) 

    state_label_editor = Label(editor, text="State: ", width=30, anchor=W)
    state_label_editor.grid(row=4, column=0, padx=20) 

    zipcode_label_editor = Label(editor, text="Zipcode: ", width=30, anchor=W)
    zipcode_label_editor.grid(row=5, column=0, padx=20) 

    #create a save button to edit a record
    edit_btn = Button(editor, text='Save Record', command=edit)
    edit_btn.grid(row=6, column=0, columnspan=2, pady=10, padx=10, ipadx=100)

    #loop througn results
    for record in records:
        f_name_editor.insert(0, record[0])
        l_name_editor.insert(0, record[1])
        address_editor.insert(0, record[2])
        city_editor.insert(0, record[3])
        state_editor.insert(0, record[4])
        zipcode_editor.insert(0, record[5])


    #commit data to database
    conn.commit()

    #close the database
    conn.close()  

#submit function for database
def submit():
    #Create and connect to database
    conn = sqlite3.connect('address_book.db')

    #create cursor
    c = conn.cursor()

    #Insert into tabel
    c.execute("INSERT INTO addresses VALUES(:f_name, :l_name, :address, :city, :state, :zipcode)",
        {
            'f_name':f_name.get(),
            'l_name':l_name.get(),
            'address':address.get(),
            'city':city.get(),
            'state':state.get(),
            'zipcode':zipcode.get(), 
        })

    #commit data to database
    conn.commit()

    #close the database
    conn.close()

    #clear the text boxes
    f_name.delete(0, END)
    l_name.delete(0, END)
    address.delete(0, END)
    city.delete(0, END)
    state.delete(0, END)
    zipcode.delete(0, END)


def query():
    #Create and connect to database
    conn = sqlite3.connect('address_book.db')

    #create cursor
    c = conn.cursor()

    #Insert into tabel
    c.execute("SELECT *, oid FROM addresses")
    records = c.fetchall() 
    
    #loop through results
    print_records = ''
    for record in records:
        print_records += str(record[0]) + " " + str(record[1]) + "\t" + str(record[6]) + "\n" 

    query_label = Label(root, text=print_records)
    query_label.grid(row=8, column=0, columnspan=2)

    #commit data to database
    conn.commit()

    #close the database
    conn.close()





#Creating text box
f_name = Entry(root, width=30)
f_name.grid(row=0, column=1, padx=20, pady=(10, 0))

l_name = Entry(root, width=30)
l_name.grid(row=1, column=1, padx=20) 

address = Entry(root, width=30)
address.grid(row=2, column=1, padx=20) 

city = Entry(root, width=30)
city.grid(row=3, column=1, padx=20) 

state = Entry(root, width=30)
state.grid(row=4, column=1, padx=20) 

zipcode = Entry(root, width=30)
zipcode.grid(row=5, column=1, padx=20) 

update_box = Entry(root, width=30)
update_box.grid(row=9, column=1)


#creating label for textbox
f_name_label = Label(root, text="First Name: ", width=30, anchor=W)
f_name_label.grid(row=0, column=0, padx=20, pady=(10, 0)) 

l_name_label = Label(root, text="Last Name: ", width=30, anchor=W)
l_name_label.grid(row=1, column=0, padx=20) 

address_label = Label(root, text="Address: ", width=30, anchor=W)
address_label.grid(row=2, column=0, padx=20) 

city_label = Label(root, text="City: ", width=30, anchor=W)
city_label.grid(row=3, column=0, padx=20) 

state_label = Label(root, text="State: ", width=30, anchor=W)
state_label.grid(row=4, column=0, padx=20) 

zipcode_label = Label(root, text="Zipcode: ", width=30, anchor=W)
zipcode_label.grid(row=5, column=0, padx=20) 

update_box_label = Label(root, text="Select ID: ")
update_box_label.grid(row=8, column=0, sticky=W, padx=(20, 0))


#Create the subbmit button
submit_button = Button(root, text="Add Record", command=submit)
submit_button.grid(row=6, column=0, columnspan=2, pady=10, padx=10, ipadx=154)

#create a query button
query_button = Button(root, text='Show Record', command=query)
query_button.grid(row=7, column=0, columnspan=3, padx=10, pady=10, ipadx=150)

#create a delete button
update_button = Button(root, text='Update Record', command=update)
update_button.grid(row=10, column=0, columnspan=3, padx=10, pady=10, ipadx=147)

root.mainloop()