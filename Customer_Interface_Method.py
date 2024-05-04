from Customer_Class import Customer

def customer_interface(restaurant_obj):
    name = input("Enter your name: ").strip()
    email = input("Enter your email: ").strip()
    phone = input("Enter your phone: ").strip()
    address = input("Enter your address: ").strip()

    # create a customer 
    cust = Customer(name = name, email = email, phone = phone, address = address)

    while True:
        print(f"\nWelcome {cust.name} to our restaurant!")
        print("1. View menu")
        print("2. Add item to cart")
        print("3. View cart")
        print("4. Pay Bill")
        print("5. Exit")

        choice = int(input("\nEnter your choice: "))
        if choice == 1:
            cust.view_menu(restaurant_obj)
    
        elif choice == 2:
            if len(restaurant_obj.menu.items) == 0:
                print("Sorry, the menu is empty. Cannot add items to the cart.\n")
            else:
                item_name = input("Enter the food item name: ").strip()
                try:
                    item_quantity = int(input("Enter the food item quantity: "))
                except:
                    print("Invalid input type! Please enter integer only!")
                    
                cust.add_to_cart(restaurant_obj, item_name, item_quantity)
 
        elif choice == 3:
            if len(restaurant_obj.menu.items) == 0:
                print("Sorry, the cart is empty. Add items to cart before!.\n")
            else:
                cust.view_cart()

        elif choice == 4:
            if len(restaurant_obj.menu.items) == 0:
                print("Sorry, the cart is empty. Add items to cart before.\n")
            else:
                cust.pay_bill()

        elif choice == 5:
            ans = input("Are you sure? (Y/N): ").strip()
            if ans.lower() == 'y':
                print("\nExited succeessfully!\n")
                break

        else:
            print("Invalid choice!!\n")
