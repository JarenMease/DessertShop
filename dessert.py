class DessertItem:
    """Superclass of the Dessert Project"""
    def __init__(self, name=""):
        self.name = name


class Candy(DessertItem):
    """Candy class defines the weight of the candy and the price per pound"""
    def __init__(self, name="", candy_weight=float, price_per_pound=float):
        super().__init__(name)
        self.candy_weight = candy_weight
        self.price_per_pound = price_per_pound


class Cookie(DessertItem):
    """Cookie class defines the amount of cookies and the price per dozen"""
    def __init__(self, name="", cookie_quantity=int, price_per_dozen=float):
        super().__init__(name)
        self.cookie_quantity = cookie_quantity
        self.price_per_dozen = price_per_dozen


class IceCream(DessertItem):
    """Ice Cream class defines the scoop count and the price per"""
    def __init__(self, name="", scoop_count=int, price_per_scoop=float):
        super().__init__(name)
        self.scoop_count = scoop_count
        self.price_per_scoop = price_per_scoop


class Sundae(IceCream, DessertItem):
    """Sundae class defines the toppings and price per"""
    def __init__(self, name="", topping_name=str, topping_price=float):
        IceCream.__init__(self, name, scoop_count=int, price_per_scoop=float)
        self.topping_name = topping_name
        self.topping_price = topping_price


class Order:
    def __init__(self):
        self.order = []

    def get_dessert_order(self):
        return self.order

    def add(self, item):
        self.order.append(item)

    def __len__(self):
        return len(self.order)








