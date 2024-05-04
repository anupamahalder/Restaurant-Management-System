class Menu:
    def __init__(self):
        self.items = [] # database for storing menu items
        
    def add_menu_item(self, item):
        self.items.append(item)

    def _find_item(self, item_name):
        for item in self.items:
            if item.name.lower() == item_name.lower():
                return item
        return None # item does not exists

    def remove_menu_item(self, item_name):
        item = self._find_item(item_name)
        if item:
            self.items.remove(item)
            print(f"{item_name} deleted successfully!\n")
        else:
            print(f"Sorry! Item not found!\n")

    def show_menu(self, restaurant):
        print(f"\n**************Menu for {restaurant.name}**************\n")
        if len(self.items) == 0:
            print("No items has added in the menu!")
            return
        print("Name\tPrice\tAvailable Quantity")
        print("-------------------------------------")
        for item in self.items:
            print(f"{item.name}\t{item.price}\t{item.quantity}")
