import dessert


Candy = dessert.Candy
Cookie = dessert.Cookie
IceCream = dessert.IceCream
Sundae = dessert.Sundae


def new_Candy():
    return Candy("test candy", 2.56, 1.50)


def new_Cookie():
    return Cookie("test cookie", 12, 12.99)


def new_IceCream():
    return IceCream("test ice cream", 3, 1.99)


def new_Sundae():
    return Sundae("test sundae", "Fudge", 1.59 )


def test_Candy():
    # testing constructor for default values
    candy = Candy()
    assert candy.name == ""
    assert candy.candy_weight == 0
    assert candy.price_per_pound == 0
    # testing constructor for non-default values
    assert new_Candy().name == "test candy"
    assert new_Candy().candy_weight == 2.56
    assert new_Candy().price_per_pound == 1.50
    # modifying attribute values for default values
    candy_mod = Candy()
    candy_mod.name = "Sweettarts"
    assert candy_mod.name == "Sweettarts"
    candy_mod.candy_weight = "2.9"
    assert candy_mod.candy_weight == "2.9"
    candy_mod.price_per_pound = "1"
    assert candy_mod.price_per_pound == "1"
    # modifying attribute values for non-default values
    candy_mod2 = new_Candy()
    candy_mod2.name = "Twix"
    assert candy_mod2.name == "Twix"
    candy_mod2.candy_weight = "3"
    assert candy_mod2.candy_weight == "3"
    candy_mod2.price_per_pound = "100"
    assert candy_mod2.price_per_pound == "100"


def test_Cookie():
    assert new_Cookie().cookie_quantity == 12
    assert new_Cookie().price_per_dozen == 12.99


def test_IceCream():
    assert new_IceCream().scoop_count == 3
    assert new_IceCream().price_per_scoop == 1.99


def test_Sundae():
    assert new_Sundae().topping_name == "Fudge"
    assert new_Sundae().topping_price == 1.59

