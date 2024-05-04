from Admin_Class import Admin
from Food_Item_Class import FoodItem
from Employee_Class import Employee

def admin_interface(restaurant_obj):
    name = input("Enter your name: ").strip()
    email = input("Enter your email: ").strip()
    phone = input("Enter your phone: ").strip()
    address = input("Enter your address: ").strip()

    # create a customer 
    admn = Admin(name = name, email = email, phone = phone, address = address)

    while True:
        print(f"\nWelcome {admn.name} to our restaurant!")
        print("1. Add New Item")
        print("2. Add New Employee")
        print("3. View Employee")
        print("4. View Menu Items")
        print("5. Delete Item")
        print("6. Exit")

        choice = int(input("\nEnter your choice: "))

        if choice == 1:
            item_name = input("Enter the food item name: ").strip()
            try:
                item_price = float(input("Enter the food item price: "))
            except:
                print("Invalid input type! Please enter number only!")
            try:
                item_quantity = int(input("Enter the food item quantity: "))
            except:
                print("Invalid input type! Please enter integer only!")
            item = FoodItem(item_name, item_price, item_quantity)
            # add item to the database 
            admn.add_new_item(restaurant_obj, item)

        elif choice == 2:
            name = input("Enter employee name: ").strip()
            email = input("Enter employee email: ").strip()
            phone = input("Enter employee phone: ").strip()
            address = input("Enter employee adress: ").strip()
            designation = input("Enter employee designation: ").strip()
            try:
                age = int(input("Enter employee age: "))
            except:
                print("Invalid input type! Please enter integer only!")
            try:
                salary = int(input("Enter employee salary: "))
            except:
                print("Invalid input type! Please enter integer only!")
            emp = Employee(name=name, email=email, phone=phone, address=address, designation=designation, age=age, salary=salary)
            admn.add_employee(restaurant_obj, emp)

        elif choice == 3:
            admn.view_employee(restaurant_obj)

        elif choice == 4:
            admn.view_menu(restaurant_obj)

        elif choice == 5:
            item_name = input("Enter the item name: ").strip()
            admn.remove_menu_item(restaurant_obj, item_name)

        elif choice == 6:
            ans = input("Are you sure? (Y/N): ").strip()
            if ans.lower() == 'y':
                print("\nExited succeessfully!\n")
                break

        else:
            print("Invalid choice!!\n")
