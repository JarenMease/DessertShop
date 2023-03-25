from abc import ABC, abstractmethod


class DessertItem(ABC):
    """Superclass of the Dessert Project"""
    def __init__(self, name="", price=float, unit=float, tax_percent=7.25):
        self.tax_percent = tax_percent
        self.name = name
        self.price = price
        self.unit = unit

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
    def __init__(self, name="", unit=float, price=float):
        super().__init__(name, unit, price)

    def calculate_cost(self):
        cost = float(self.price) * float(self.unit)
        return cost

    def __str__(self):
        return {f"{self.name}, {self.unit}lbs, ${self.price()}/lb, ${self.calculate_cost()}, "
                f"${self.calculate_tax()}"}


class Cookie(DessertItem):
    """Cookie class defines the amount of cookies and the price per dozen"""
    def __init__(self, name="", unit=float, price=float):
        super().__init__(name, unit, price)

    def calculate_cost(self):
        cost = ((float(self.price) / 12) * float(self.unit))
        return cost

    def __str__(self):
        return {f"{self.name}, {self.unit}/cookies, {self.price()}/dozen, ${self.calculate_cost()},"
                f"${self.calculate_tax()}"}


class IceCream(DessertItem):
    """Ice Cream class defines the scoop count and the price per"""
    def __init__(self, name="", unit=float, price=float):
        super().__init__(name, unit, price)

    def calculate_cost(self):
        cost = float(self.price) * float(self.unit)
        return cost

    def __str__(self):
        return {f"{self.name}, {self.unit}/scoops, {self.price}/scoop, ${self.calculate_cost()}, "
                f"${self.calculate_tax()}"}


class Sundae(IceCream, DessertItem):
    """Sundae class defines the toppings and price per"""
    def __init__(self, name="", unit=int, price=float, topping_name="", topping_price=float):
        super().__init__((topping_name + " " + name + " Sundae"), unit, price)
        self.topping_name = topping_name
        self.topping_price = topping_price

    def calculate_cost(self):
        cost = (float(self.price) * float(self.unit)) + float(self.topping_price)
        return cost

    def __str__(self):
        return {f" {self.name}, {self.unit}/scoops, {self.price}/scoop, ${self.calculate_cost()}, "
                f"${self.calculate_tax()} \n{self.topping_name}, 1, ${self.topping_price}"}


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

    def item_count(self):
        return len(self.order)

    def __str__(self):
        for item in self.order:
            return {f" {self.add(item)}, {round(item.calculate_cost(), 2)}, {round(item.calculate_tax(), 2)}"}

    def __len__(self):
        return len(self.order)
