import os
from datetime import date

# Console Inventory Program Demo
print("\t\t\t\t\t\t\t\t\t\t Welcome To The Baker's Shop")
print("\n")
print("Please take a moment to introduce yourself before continue.")
print("\n")
print("Enter your FirstName: ")
firstName = input()
print("Enter your LastName: ")
lastName = input()
print("Enter your phone number: ")
phoneNumber = input()
print("Enter your choice 1....")
choice_1 = input()
print("Enter your choice 2....")
choice_2 = input()
print("Enter your username: ")
userName = input()
print("Enter your password")
password = input()

os.system('cls')

print("\t\t\t\t\t\t\t\t\tHello " + firstName + " " + lastName + " " + "Welcome to the Baker's Shoppe.")
print("Enter your username to continue...")
userNameLogin = input()
if userNameLogin == userName:
    print("Enter your password to continue...")
    passwordVerfication = input()
if passwordVerfication == password:
    print("\t\t\t\t\t\t\t\t\tYou've logged in successfully. Press 1 to proceed with your order")
    confirmation = input()
if confirmation == str(1):
    print("\t\t\t\t\t\t\t\t\tWe have listed few items from your choices.")
    print("\nThis was your first choice : "+ choice_1+" "+"INR 50.00")
    print("\nThis was your second choice : "+ choice_2+" "+"INR 100.00")
    print("\nPress 1 for choice_1: "+ choice_1 + "")
    choosenNo = input()
if choosenNo == str(1):
    print("\nEnter Quantity for " + choice_1)
    quantity_1 = input()
    print("Your Total amount is: " + str(50*int(quantity_1)) + "\nPlease Pay" + str(50*int(quantity_1)) + "Rs. in cash.")
    print("Thanks " + firstName + " " + lastName + " For Shopping with Baker's Shop \n Please Come again")

else:
    print("Wrong password")

