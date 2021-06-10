from tkinter import * 

root = Tk()
root.title("Registration Form")
root.geometry("400x500")
# root.configure(background='pink')


first_name_label = Label(root, text="First Name: ", bg='pink', font="courier 14 bold")
last_name_label = Label(root, text="Lant Name: ", bg='pink', font="courier 14 bold")
username_label = Label(root, text="Username: ", bg='pink', font="courier 14 bold")
email_label = Label(root, text="Email: ", bg='pink', font="courier 14 bold")
password_label = Label(root, text="Password: ", bg='pink', font="courier 14 bold")
confirm_password_label = Label(root, text="Confirm: ", bg='pink', font="courier 14 bold")

first_name_label.grid(row=0, column=0, padx=20, pady=10)
last_name_label.grid(row=1, column=0, padx=20, pady=10)
username_label.grid(row=2, column=0, padx=20, pady=10)
email_label.grid(row=3, column=0, padx=20, pady=10, )
password_label.grid(row=4, column=0, padx=20, pady=10)
confirm_password_label.grid(row=5, column=0, padx=20, pady=10)


first_name_entry = Entry(root, text="First Name: ")
last_name_entry = Entry(root, text="Lant Name: ")
username_entry = Entry(root, text="Username: ")
email_entry = Entry(root, text="Email: ")
password_entry = Entry(root, text="Password: ")
confirm_password_entry = Entry(root, text="Confirm: ")

first_name_entry.grid(row=0, column=1)
last_name_entry.grid(row=1, column=1)
username_entry.grid(row=2, column=1)
email_entry.grid(row=3, column=1)
password_entry.grid(row=4, column=1)
confirm_password_entry.grid(row=5, column=1)






root.mainloop()
Label(root, text="Registar Now!", bg="pink", fg="#000000", bd=1, font="cursive 25 bold", pady=10, padx=10, width=100).grid()