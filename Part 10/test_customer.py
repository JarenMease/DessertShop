import uuid
import dessertshop
import test_dessert

"""
I am aware that these test cases give a warning. It is from importing dessertshop.
I am not sure why this file is giving a deprecation warning. Nonetheless, the 
test cases still pass.
"""


def test_customer_attributes():
    customer = dessertshop.Customer("Jaren")
    assert customer.customer_name == "Jaren"
    assert customer.order_history == []
    assert isinstance(customer.customer_id, uuid.UUID)


def test_add2history():
    customer = dessertshop.Customer("Jaren")
    order = test_dessert.new_Order()
    customer.add2history(order)
    assert customer.order_history[0] == order
    assert len(customer.order_history) == 1
