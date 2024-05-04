from User_Class import User
from Customer_Class import Customer
from Admin_Class import Admin
from Menu_Class import Menu
from Order_Class import Order
from Restaurant_Class import Restaurant
from Food_Item_Class import FoodItem
from Customer_Interface_Method import customer_interface
from Admin_Interface_Method import admin_interface

# make a global restaurant 
royal_restaurant = Restaurant("Royal Restaurant")

while True:
    print("\nWelcome")
    print("1. Customer")
    print("2. Admin")
    print("3. Exit")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        # call the customer interface 
        customer_interface(royal_restaurant)

    elif choice == 2:
        admin_interface(royal_restaurant)

    elif choice == 3:
        ans = input("Are you sure? (Y/N): ").strip()
        if ans.lower() == 'y':
            print("\nExited succeessfully!\n")
            break

    else:
        print("Invalid input!\n")
