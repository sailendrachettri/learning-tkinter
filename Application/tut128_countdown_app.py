from tkinter import * 
from datetime import date

root = Tk()
root.title('Tkinter GUI - Sailendra')
root.geometry('400x400')

panci = Label(root, text="DON'T PANIC!", font=("Times New Roman", "35", "bold"), bg="black", fg="green")
panci.pack(pady=20, ipadx=10, ipady=10) 

# Get date
today = date.today()

# format date
f_today = today.strftime("%A - %B %d, %Y")

# Output date
today_label = Label(root, text=f_today)
today_label.pack(pady=20) 

#Countdown
days_in_year = 365
todays_day_number = int(today.strftime("%j"))

# Calculate days left in year
days_left = days_in_year - todays_day_number
countdown_label = Label(root, text=f"There are only {days_left} Days\nLeft in 2021!", font=("Times New Roman", "25", "bold"))
countdown_label.pack(pady=10) 

root.mainloop()