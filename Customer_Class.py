from User_Class import User
from Order_Class import Order

class Customer(User):
    def __init__(self, name, email, phone, address):
        super().__init__(name, email, phone, address)
        # cart is an instance of Oder class 
        # means with the help of self.cart we can use all the properties and methods of Order class 
        self.cart = Order() 

    def view_menu(self, restaurant):
        restaurant.menu.show_menu(restaurant)

    def add_to_cart(self, restaurant, item_name, quantity):
        item = restaurant.menu._find_item(item_name)
        if item:
            if quantity > item.quantity:
                print("Item quantity exceeded!\n")
            else:
                # replacing the existing quantity by user's given quantity 
                item.quantity = quantity
                self.cart.add_item(item)
                print("Item added successfully!")
        else:
            print("Item not found")

    def view_cart(self):  
        if self.cart.total_price == 0:
            print("Sorry! No items found in your cart, please add items to the cart before!")
            return  
        print("\n************View Cart************")
        print("\nName\tPrice\tQuantity")
        print("-----------------------------------")
        for item, quantity in self.cart.items.items():
            print(f"{item.name}\t{item.price}\t{quantity}")
        print(f"\nTotal Price: {self.cart.total_price}\n")

    def pay_bill(self):
        if self.cart.total_price == 0:
            print("Nothing to pay! Please add any items to the cart!\n")
        else:
            print(f"Total {self.cart.total_price} has paid successfully!")
            # clear the cart 
            self.cart._clear()
