
class Order:
    def __init__(self):
        self.items = {} # database for oder details

    def add_item(self, item):
        if item in self.items:
            # if item is in cart already then only quantity will be updated 
            self.items[item] += item.quantity
        else:
            self.items[item] = item.quantity

    def remove_from_cart(self, item):
        if item in self.items:
            del self.items[item]

    # make it as property
    @property
    def total_price(self):
        return sum(item.price*quantity for item, quantity in self.items.items())

    def _clear(self):
        self.items = {}
