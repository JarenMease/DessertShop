from dessert import Candy, Cookie, IceCream, Sundae, Order
import receipt
from freeze import Freezer


def main_menu():
    my_order = Order()
    order_formatted = []
    freezer = Freezer()

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

        else:
            print("Please enter a valid option!")
            continue
        return my_order

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

    for item in my_order.order:
        if isinstance(item, Freezer):
            freezer.take(item.name)

    import pandas as pd
    df = pd.DataFrame(order_formatted)
    print(df.to_string(index=False))

    receipt.make_receipt(order_formatted)


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
