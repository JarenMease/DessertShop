from abc import ABC, abstractmethod


class DessertItem(ABC):
    """Superclass of the Dessert Project"""
    def __init__(self, name="", price=float, tax_percent=7.25):
        self.tax_percent = tax_percent
        self.name = name
        self.price = price

    @abstractmethod
    def calculate_cost(self):
        total_price = self.price
        return float(total_price)

    def calculate_tax(self):
        tax_rate = self.tax_percent / 100
        total_cost = float(self.calculate_cost()) * tax_rate
        return total_cost


class Candy(DessertItem):
    """Candy class defines the weight of the candy and the price per pound"""
    def __init__(self, name="", price=float, candy_weight=float):
        super().__init__(name, price)
        self.candy_weight = candy_weight

    def calculate_cost(self):
        cost = float(self.price) * float(self.candy_weight)
        return cost


class Cookie(DessertItem):
    """Cookie class defines the amount of cookies and the price per dozen"""
    def __init__(self, name="", cookie_quantity=int, price=float):
        super().__init__(name, price)
        self.cookie_quantity = cookie_quantity

    def calculate_cost(self):
        cost = float(self.price) * float(self.cookie_quantity)/12
        return cost


class IceCream(DessertItem):
    """Ice Cream class defines the scoop count and the price per"""
    def __init__(self, name="", scoop=float, price=float):
        super().__init__(name, price)
        self.scoop = scoop

    def calculate_cost(self):
        cost = float(self.price) * float(self.scoop)
        return cost


class Sundae(IceCream, DessertItem):
    """Sundae class defines the toppings and price per"""
    def __init__(self, name="", scoop=float, price=float, topping_name="", topping_price=float):
        # my_order.add(Sundae("Vanilla", 3, .69, "Hot Fudge", 1.29))
        super().__init__(name, scoop, price)
        # IceCream(scoop)
        self.topping_name = topping_name
        self.topping_price = topping_price

    def calculate_cost(self):
        cost = float(self.price) * float(self.scoop) + float(self.topping_price)
        return cost


class Order:
    def __init__(self):
        self.order = []

    def get_dessert_order(self):
        return self.order

    def add(self, item):
        self.order.append(item)

    def order_cost(self):
        cost = 0
        for item in self.order:
            cost += item.calculate_cost()
        return cost

    def order_tax(self):
        tax = 0
        for item in self.order:
            tax += item.calculate_tax()
        return tax

    def __len__(self):
        return len(self.order)








