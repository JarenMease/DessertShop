from dessert import Order, Candy, Cookie, IceCream, Sundae, DessertItem

"""py_tests can be ran with python -m pytest test_dessert.py in the Terminal"""


def new_candy():
    return Candy("test candy", 1.50, 2.56)


def new_cookie():
    return Cookie("test cookie", 12, 12.99)


def new_ice_cream():
    return IceCream("test ice cream", 3, 1.99)


def new_sundae():
    return Sundae("test sundae", 3, .69, "test topping", 1.29)


def test_candy():
    assert new_candy().name == "test candy"
    assert new_candy().price == 1.5
    assert new_candy().candy_weight == 2.56


def test_cookie():
    assert new_cookie().name == "test cookie"
    assert new_cookie().cookie_quantity == 12
    assert new_cookie().price == 12.99


def test_icecream():
    assert new_ice_cream().name == "test ice cream"
    assert new_ice_cream().scoop == 3
    assert new_ice_cream().price == 1.99


def test_sundae():
    assert new_sundae().name == "test sundae"
    assert new_sundae().scoop == 3
    assert new_sundae().price == 0.69
    assert new_sundae().topping_name == "test topping"
    assert new_sundae().topping_price == 1.29













