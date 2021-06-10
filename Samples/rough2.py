# ----------------------------------------SOLUTION 4----------------------------------------

def convert():
    celsius = int(input("\nEnter temprature in calsius: "))
    faherenheit = (celsius * 9/5) + 32
    print(celsius, " celsius is equal to ", faherenheit, " faherenheit.\n")


convert()

while(True):
    user_choice = str(input("Do you want to convert again?\npress 'y' for yes\npress 'n' for no\n"))

    if(user_choice == 'y'):
        convert()
    else:
        print("\nHave a good day!")
        break

