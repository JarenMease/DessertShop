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
    
    order_formatted.append(["-------------------", "", ""])
    order_formatted.append(["Order Subtotals:", "$" + str(round(my_order.order_cost(), 2)), "$" + str(round(my_order.order_tax(), 2))])
    order_formatted.append(["Order Total:", "", "$" + str(round(my_order.order_cost() + my_order.order_tax(), 2))])
    order_formatted.append(["Total number of items in the order:", "", len(my_order)])

    receipt.make_receipt(order_formatted)
    # Print out the total number of items in the order

    # print("Order Subtotals:", round(my_order.order_cost(), 2), round(my_order.order_tax(), 2))
    # print("Order Total:", round(my_order.order_cost() + my_order.order_tax(), 2))
    #
    # print("Total number of items in the order:", len(my_order))
    

if __name__ == "__main__":
    main()


