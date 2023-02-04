from dessert import Candy, Cookie, IceCream, Sundae, DessertItem

"""py_tests can be ran with python -m pytest test_dessert.py in the Terminal"""

def new_Candy():
    return Candy("test candy", 2.56, 1.50)


def new_Cookie():
    return Cookie("test cookie", 12, 12.99)


def new_IceCream():
    return IceCream("test ice cream", 3, 1.99)


def new_Sundae():
    return Sundae("test sundae", "Fudge", 1.59 )


def test_Candy():
    assert new_Candy().candy_weight == 2.56
    assert new_Candy().price_per_pound == 1.50


def test_Cookie():
    assert new_Cookie().cookie_quantity == 12
    assert new_Cookie().price_per_dozen == 12.99


def test_IceCream():
    assert new_IceCream().scoop_count == 3
    assert new_IceCream().price_per_scoop == 1.99


def test_Sundae():
    assert new_Sundae().topping_name == "Fudge"
    assert new_Sundae().topping_price == 1.59


# def test_constructor():
#     # Test with a name passed in
#     candy = DessertItem("Reese's Egg")
#     assert candy.name == "Reese's Egg"
#
#     # Test with no name passed in
#     candy = DessertItem()
#     assert candy.name == ""








