from tkinter import * 
import mysql.connector
import csv
from tkinter import ttk


root = Tk()
root.title('Tkinter GUI - Sailendra')
root.geometry('400x600')

mydb = mysql.connector.connect(
    host = "localhost",
    user = "sailendra",
    password = "!1o1//SAnot:@",
    database = "codemy"
)

#create cursor
my_cursor = mydb.cursor() 


def clear_fields():
    first_name_box.delete(0, END)
    last_name_box.delete(0, END)
    email_box.delete(0, END)
    address_1_box.delete(0, END)
    address_2_box.delete(0, END)
    city_box.delete(0, END)
    state_box.delete(0, END)
    zipcode_box.delete(0, END)
    country_box.delete(0, END)
    phone_box.delete(0, END)
    payment_method_box.delete(0, END)
    discount_code_box.delete(0, END)
    price_paid_box.delete(0, END)

def add_customer():
    sql_command = "INSERT INTO customers (first_name, last_name, zipcode, price_paid, email, address_1, address_2, city, state, country, phone, payment_method, discount_code) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"
    values = (first_name_box.get(), last_name_box.get(), zipcode_box.get(), price_paid_box.get(), email_box.get(), address_1_box.get(), address_2_box.get(), city_box.get(), state_box.get(), country_box.get(), phone_box.get(), payment_method_box.get(), discount_code_box.get())
    my_cursor.execute(sql_command, values)

    #commit changes
    mydb.commit()
    mydb.close()

    first_name_box.delete(0, END)
    last_name_box.delete(0, END)
    address_1_box.delete(0, END)
    address_2_box.delete(0, END)
    city_box.delete(0, END)
    state_box.delete(0, END)
    zipcode_box.delete(0, END)
    country_box.delete(0, END)
    phone_box.delete(0, END)
    email_box.delete(0, END)
    payment_method_box.delete(0, END)
    discount_code_box.delete(0, END)
    price_paid_box.delete(0, END)

def write_to_csv(result):
    with open('customers.csv', 'a') as f:
        w = csv.writer(f, dialect='excel') 
        for record in result:
            w.writerow(record) 

def search_customers():
    search_customers = Tk()
    search_customers.title("Search of All Customer")
    # search_customers.geometry("400x400") 

    def search_now():
        searched = search_box.get()
        sql = "SELECT * FROM customers WHERE last_name=%s"

        name = (searched, ) 
        result = my_cursor.execute(sql, name)
        result = my_cursor.fetchall() 

        if not result:
            result = "Record not found..."

        searched_label = Label(search_customers, text=result[0])
        searched_label.grid(row=2, column=0, padx=10) 

    #extry box to search for customer
    search_box = Entry(search_customers)
    search_box.grid(row=0, column=1, padx=10, pady=10) 

    #search box label
    search_box_label = Label(search_customers, text="Search Customer by last name")
    search_box_label.grid(row=0, column=0, padx=10, pady=10)

    #search button for customers
    search_button = Button(search_customers, text="Search Customers", command=search_now)
    search_button.grid(row=1, column=0, padx=10) 

def list_customer():
    list_customer_query = Tk()
    list_customer_query.title("List of All Customer")
    list_customer_query.geometry("900x400") 

    #query the database
    my_cursor.execute("SELECT * FROM customers")
    result = my_cursor.fetchall()
    for index, x in enumerate(result):
        num = 0
        for y in x:
            lookup_label = Label(list_customer_query, text=y)
            lookup_label.grid(row=index, column=num)
            num += 1 
        
    csv_button = Button(list_customer_query, text="Save to Excel", command=lambda: write_to_csv(result))
    csv_button.grid(row=index+1, column=0)


#Create a Label
title_label = Label(root, text="Codemy Customer Database", font="Helvetica 16 bold")
title_label.grid(row=0, column=0, columnspan=2)

#create main form to enter customer data
first_name_label = Label(root, text="First Name").grid(row=1, column=0, sticky=W,padx=10)
last_name_label = Label(root, text="Last Name").grid(row=2, column=0, sticky=W,padx=10)
address_1_label = Label(root, text="Address 1").grid(row=3, column=0, sticky=W,padx=10)
address_2_label = Label(root, text="Address 2").grid(row=4, column=0, sticky=W,padx=10)
city_label = Label(root, text="City").grid(row=5, column=0, sticky=W,padx=10)
state_label = Label(root, text="State").grid(row=6, column=0, sticky=W,padx=10)
zipcode_label = Label(root, text="Zipcode").grid(row=7, column=0, sticky=W,padx=10)
country_label = Label(root, text="Country").grid(row=8, column=0, sticky=W,padx=10)
phone_label = Label(root, text="Phone").grid(row=9, column=0, sticky=W,padx=10)
email_label = Label(root, text="Email").grid(row=10, column=0, sticky=W,padx=10)
payment_method_label = Label(root, text="Payment method").grid(row=11, column=0, sticky=W,padx=10)
discount_code_label = Label(root, text="Discount code").grid(row=12, column=0, sticky=W,padx=10)
price_paid_label = Label(root, text="Price Paid").grid(row=13, column=0, sticky=W,padx=10)

#create entry boxes
first_name_box = Entry(root)
first_name_box.grid(row=1, column=1, pady=5)

last_name_box = Entry(root)
last_name_box.grid(row=2, column=1, pady=5)

address_1_box = Entry(root)
address_1_box.grid(row=3, column=1, pady=5)

address_2_box = Entry(root)
address_2_box.grid(row=4, column=1, pady=5)

city_box = Entry(root)
city_box.grid(row=5, column=1, pady=5)

state_box = Entry(root)
state_box.grid(row=6, column=1, pady=5)

zipcode_box = Entry(root)
zipcode_box.grid(row=7, column=1, pady=5)

country_box = Entry(root)
country_box.grid(row=8, column=1, pady=5)

phone_box = Entry(root)
phone_box.grid(row=9, column=1, pady=5)

email_box = Entry(root)
email_box.grid(row=10, column=1, pady=5)

payment_method_box = Entry(root)
payment_method_box.grid(row=11, column=1, pady=5)

discount_code_box = Entry(root)
discount_code_box.grid(row=12, column=1, pady=5)

price_paid_box = Entry(root)
price_paid_box.grid(row=13, column=1, pady=5)

# Create Button
add_customer_button = Button(root, text="Add Customer to Database", command=add_customer)
add_customer_button.grid(row=14, column=0, pady=10, padx=10)

clear_button_fields = Button(root, text="Clear Fields", command=clear_fields)
clear_button_fields.grid(row=14, column=1)

list_customer_button = Button(root, text="List Customer", command=list_customer)
list_customer_button.grid(row=15, column=0, sticky=W, padx=10)

#Search customers
search_customer_button = Button(root, text="Search Customer", command=search_customers)
search_customer_button.grid(row=15, column=1, sticky=W, padx=10)


root.mainloop() 
