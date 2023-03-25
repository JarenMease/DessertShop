import random

from dessert import Candy, Cookie, IceCream, Sundae, Order
import receipt
from freeze import Freezer
from payment import PayType, Payment
from typing import Dict


class Customer:
    def __init__(self, customer_name: str):
        self.customer_name = customer_name
        self.order_history = []
        self.customer_id = random.randint(1000, 9999)

    def add2history(self, order) -> 'Customer':
        self.order_history.append(order)
        return self


def main_menu():
    default_payment = PayType.CASH
    freezer = Freezer()

    while True:
        my_order = Order(default_payment)
        order_formatted = []
        customer_db: Dict[str, Customer] = {}

        while True:
            print("1: Candy\n2: Cookie\n3: Ice Cream\n4: Sundae\n"
                  "What would you like to add to the order? (1-4, Enter for done): ")
            choice = input().strip()
            if not choice:
                break

            if choice == "1":
                item = user_prompt_candy()
                if item:
                    my_order.add(item)
                    continue

            elif choice == "2":
                item = user_prompt_cookie()
                if item:
                    my_order.add(item)
                    continue

            elif choice == "3":
                item = user_prompt_ice_cream()
                if item:
                    my_order.add(item)
                    continue

            elif choice == "4":
                item = user_prompt_sundae()
                if item:
                    my_order.add(item)
                    continue

        while True:
            customer_name = input("Enter customer name: ")
            if customer_name not in customer_db:
                customer = Customer(customer_name)
                customer_db[customer_name] = customer
            else:
                customer = customer_db[customer_name]
                break

            customer.add2history(my_order)
            continue

        while True:
            print("1: Cash\n2: Card\n3: Phone\n")
            choice = input("Enter a Payment Type: ")
            if choice == "1" or choice == "2" or choice == "3":
                my_order.set_pay_method(int(choice))
                break
            elif choice == "":
                my_order.set_pay_method(1)
                break
            else:
                print("Please enter a valid choice!")
                continue

        my_order.order.sort(key=lambda x: x.calculate_cost())

        # Stock the freezer with some freezable items
        freezer.put(Cookie("Oatmeal Raisin Cookies", 8))
        freezer.put(Cookie("Chocolate Chip Cookies", 12))
        freezer.put(IceCream("Pistachio Ice Cream", 4))
        freezer.put(IceCream("Vanilla Ice Cream", 12))
        freezer.put(Sundae("Hot Fudge Topping", 12))

        order_formatted.append(["Name", "Quantity", "Unit Price", "Cost", "Tax", ])

        for item in my_order.order:
            if isinstance(item, Sundae):
                order_formatted.append([item.name + " (" + item.packaging + ")", str(int(item.unit)) + " scoops", "$" + str(item.price) + "/scoop",
                                        "$" + str(round(item.calculate_cost(), 2)),
                                        "$" + str(round(item.calculate_tax(), 2))])
                order_formatted.append(
                    [item.topping_name, str(round(item.unit, 1)), "$" + str(item.topping_price), " ", " "])
            elif isinstance(item, Cookie):
                order_formatted.append([item.name + " (" + item.packaging + ")", str(int(item.unit)) + " cookies", "$" + str(item.price) + "/dozen",
                                        "$" + str(round(item.calculate_cost(), 2)),
                                        "$" + str(round(item.calculate_tax(), 2))])
            elif isinstance(item, Candy):
                order_formatted.append([item.name + " (" + item.packaging + ")", str(round(item.unit, 1)) + "lbs", "$" + str(item.price) + "/lb",
                                        "$" + str(round(item.calculate_cost(), 2)),
                                        "$" + str(round(item.calculate_tax(), 2))])
            elif isinstance(item, IceCream):
                order_formatted.append([item.name + " (" + item.packaging + ")", str(int(item.unit)) + " scoops", "$" + str(item.price) + "/scoop",
                                        "$" + str(round(item.calculate_cost(), 2)),
                                        "$" + str(round(item.calculate_tax(), 2))])
            else:
                order_formatted.append([item.name + " (" + item.packaging + ")", str(item.unit), "$" + str(item.price),
                                        "$" + str(round(item.calculate_cost(), 2)),
                                        "$" + str(round(item.calculate_tax(), 2))])

        order_formatted.append(["Total number of items in the order:", len(my_order), "", "", ""])

        order_formatted.append(["Order Subtotals:", " ", "$" + str(round(my_order.order_cost(), 2)),
                                "$" + str(round(my_order.order_tax(), 2)), " "])
        order_formatted.append(
            ["Order Total:", " ", " ", "$" + str(round(my_order.order_cost() + my_order.order_tax(), 2)), " "])

        order_formatted.append(["Paid with " + my_order.get_payment_method(), " ", " ", " ", " "])

        order_formatted.append(["Customer Name: " + str(customer_name), " ", " ", " ", " "])

        order_formatted.append(["Customer ID: " + str(customer.customer_id), " ", " ", " ", " " ])

        for item in my_order.order:
            if isinstance(item.name, Freezer):
                freezer.take(item)

        import pandas as pd
        df = pd.DataFrame(order_formatted)
        print(df.to_string(index=False))

        receipt.make_receipt(order_formatted)

        print("Start another order? (y/n): ")
        choice = input().strip().lower()
        if choice != "y":
            break


def user_prompt_candy():
    print("Enter the type of candy: ")
    name = input().strip()
    print("Enter the weight: ")
    weight = float(input().strip())
    print("Enter the price per pound: ")
    price = float(input().strip())
    return Candy(name, weight, price)


def user_prompt_cookie():
    print("Enter the type of cookie: ")
    name = input().strip()
    print("Enter the quantity purchased: ")
    quantity = float(input().strip())
    print("Enter the price per dozen: ")
    price = float(input().strip())
    return Cookie(name, quantity, price)


def user_prompt_ice_cream():
    print("Enter the type of ice cream: ")
    name = input().strip()
    print("Enter the number of scoops: ")
    scoop = float(input().strip())
    print("Enter the price per scoop: ")
    price = float(input().strip())
    return IceCream(name, scoop, price)


def user_prompt_sundae():
    print("Enter the type of ice cream: ")
    name = input().strip()
    print("Enter the number of scoops: ")
    scoop = float(input().strip())
    print("Enter the price per scoop: ")
    price = float(input().strip())
    print("Enter the topping: ")
    topping_name = input().strip()
    print("Enter the price for the topping: ")
    topping_price = float(input().strip())
    return Sundae(name, scoop, price, topping_name, topping_price)


if __name__ == "__main__":
    main_menu()
