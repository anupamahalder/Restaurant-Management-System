from users import User
# Creted Admin class by inheriting an abstract class named User
class Admin(User):
    def __init__(self, name, email, phone, address):
        super().__init__(name, email, phone, address)

    def add_employee(self, restaurant, employee):
        # name of the restaurant will be passed 
        restaurant.add_employee(employee)

    def view_employee(self, restaurant):
        restaurant.view_employee()
    
    def add_new_item(self, restaurant, item):
        restaurant.menu.add_menu_item(item)
        
    def remove_menu_item(self, restaurant, item):
        restaurant.menu.remove_menu_item(item)
    
    def view_menu(self, restaurant):
        restaurant.menu.show_menu(restaurant)
