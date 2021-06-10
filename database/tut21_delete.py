from tkinter import * 
import sqlite3

root = Tk()
root.title('Tkinter GUI - Sailendra')


#function to delete the record
def delete():
    #Create and connect to database
    conn = sqlite3.connect('address_book.db')

    #create cursor
    c = conn.cursor()

    #delete  a record
    c.execute(f"DELETE from addresses WHERE oid={delete_box.get()}") 
    oid.delete(0, END)

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

delete_box = Entry(root, width=30)
delete_box.grid(row=9, column=1)


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


delete_box_label = Label(root, text="Delete ID: ")
delete_box_label.grid(row=8, column=0, sticky=W, padx=(20, 0))


#Create the subbmit button
submit_button = Button(root, text="Add Record", command=submit)
submit_button.grid(row=6, column=0, columnspan=2, pady=10, padx=10, ipadx=154)

#create a query button
query_button = Button(root, text='Show Record', command=query)
query_button.grid(row=7, column=0, columnspan=3, padx=10, pady=10, ipadx=150)

#create a delete button
delete_button = Button(root, text='Delete Record', command=delete)
delete_button.grid(row=10, column=0, columnspan=3, padx=10, pady=10, ipadx=147)

root.mainloop()