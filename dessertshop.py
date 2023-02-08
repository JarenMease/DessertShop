from dessert import Candy, Cookie, IceCream, Sundae, Order
import receipt


def main():
    my_order = Order()
    order_formatted = []

    my_order.add(Candy("Candy Corn", 1.5, .25))
    my_order.add(Candy("Gummy Bears", .25, .35))
    my_order.add(Cookie("Chocolate Chip", 6, 3.99))
    my_order.add(IceCream("Pistachio", 2, .79))
    my_order.add(Sundae("Vanilla", 3, .69, "Hot Fudge", 1.29))
    my_order.add(Cookie("Oatmeal Raisin", 2, 3.45))

    # for item in my_order.order:
    #     print(item.name, round(item.calculate_cost(), 2), round(item.calculate_tax(),2))

    order_formatted.append(["Name", "Cost", "Tax"])

    for item in my_order.order:
        order_formatted.append([item.name, "$" + str(round(item.calculate_cost(), 2)), "$" + str(round(item.calculate_tax(), 2))])

    order_formatted.append(["Order Subtotals:", "$" + str(round(my_order.order_cost(), 2)), "$" + str(round(my_order.order_tax(), 2))])
    order_formatted.append(["Order Total:", "", "$" + str(round(my_order.order_cost() + my_order.order_tax(), 2))])
    order_formatted.append(["Total number of items in the order:", "", len(my_order)])

    receipt.make_receipt(order_formatted)
    # Print out the total number of items in the order

    # print("Order Subtotals:", round(my_order.order_cost(), 2), round(my_order.order_tax(), 2))
    # print("Order Total:", round(my_order.order_cost() + my_order.order_tax(), 2))
    #
    # print("Total number of items in the order:", len(my_order))


def main_menu():
    my_order = Order()
    order_formatted = []

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

    # for item in my_order.order:
    #     print(item.name, round(item.calculate_cost(), 2), round(item.calculate_tax(),2))
    #
    # Print out the total number of items in the order
    #
    # print("Order Subtotals:", round(my_order.order_cost(), 2), round(my_order.order_tax(), 2))
    # print("Order Total:", round(my_order.order_cost() + my_order.order_tax(), 2))
    #
    # print("Total number of items in the order:", len(my_order))

    order_formatted.append(["Name", "Cost", "Tax"])

    for item in my_order.order:
        order_formatted.append([item.name, round(item.calculate_cost(), 2), round(item.calculate_tax(), 2)])

    order_formatted.append(["Order Subtotals:", round(my_order.order_cost(), 2), round(my_order.order_tax(), 2)])
    order_formatted.append(["Order Total:", "", round(my_order.order_cost() + my_order.order_tax(), 2)])
    order_formatted.append(["Total number of items in the order:", "", len(my_order)])

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


