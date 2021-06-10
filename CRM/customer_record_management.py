from tkinter import * 
import mysql.connector

root = Tk()
root.title('Tkinter GUI - Sailendra')
root.geometry('400x400')

mydb = mysql.connector.connect(
    host = "localhost",
    user = "sailendra",
    password = "!1o1//SAnot:@",
    database = "codemy"
)
# print(mydb) 

#create cursor
my_cursor = mydb.cursor() 

#creating database
#my_cursor.execute("CREATE DATABASE codemy")

#checking if database is created or not
# my_cursor.execute("SHOW DATABASES")
# for db in my_cursor:
#     print(db) 

#create table
#my_cursor.execute("CREATE TABLE customers (first_name VARCHAR(225), last_name VARCHAR(225), zipcode INT(10), price_paid DECIMAL(10, 2), user_id INT AUTO_INCREMENT PRIMARY KEY)")

#show table
my_cursor.execute("SELECT * FROM s")
# print(my_cursor.description)
for item in my_cursor.description:
    print(item)




root.mainloop()