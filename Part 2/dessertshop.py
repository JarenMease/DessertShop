from dessert import Candy, Cookie, IceCream, Sundae, Order


def main():
    my_order = Order()

    my_order.add(Candy("Candy Corn", 1.5, .25))
    my_order.add(Candy("Gummy Bears", .25, .35))
    my_order.add(Cookie("Chocolate Chip", 6, 3.99))
    my_order.add(IceCream("Pistachio", 2, .79))
    my_order.add(Sundae("Vanilla", 3, .69, "Hot Fudge", 1.29))
    my_order.add(Cookie("Oatmeal Raisin", 2, 3.45))

    for item in my_order.order:
        print(item.name)

    print("Total number of items in the order:", len(my_order))


if __name__ == "__main__":
    main()
