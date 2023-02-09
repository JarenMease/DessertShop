class DessertItem:
    """Superclass of the Dessert Project"""
    def __init__(self, name=""):
        self.name = name
        pass

    def __str__(self):
        pass


class Candy(DessertItem):
    """Candy class defines the weight of the candy and the price per pound"""
    def __init__(self, name="", candy_weight=0.0, price_per_pound=0.0):
        super().__init__(name)
        self.candy_weight = candy_weight
        self.price_per_pound = price_per_pound


class Cookie(DessertItem):
    """Cookie class defines the amount of cookies and the price per dozen"""
    def __init__(self, name="", cookie_quantity=0, price_per_dozen=0.0):
        super().__init__(name)
        self.cookie_quantity = cookie_quantity
        self.price_per_dozen = price_per_dozen


class IceCream(DessertItem):
    """Ice Cream class defines the scoop count and the price per"""
    def __init__(self, name="", scoop_count=0, price_per_scoop=0.0):
        super().__init__(name)
        self.scoop_count = scoop_count
        self.price_per_scoop = price_per_scoop


class Sundae(IceCream, DessertItem):
    """Sundae class defines the toppings and price per"""
    def __init__(self, name="", scoop_count=0, price_per_scoop=0.0, topping_name="", topping_price=0.0):
        super().__init__(name, scoop_count, price_per_scoop)
        self.topping_name = topping_name
        self.topping_price = topping_price
