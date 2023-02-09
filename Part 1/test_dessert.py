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
    return Sundae("test sundae", "Fudge", 1.59)


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
    # testing constructor for default values
    cookie = Cookie()
    assert cookie.name == ""
    assert cookie.cookie_quantity == 0
    assert cookie.price_per_dozen == 0
    # testing constructor for non-default values
    assert new_Cookie().name == "test cookie"
    assert new_Cookie().cookie_quantity == 12
    assert new_Cookie().price_per_dozen == 12.99
    # modifying attribute values for default values
    cookie_mod = Cookie()
    cookie_mod.name = "Chocolate Chip"
    assert cookie_mod.name == "Chocolate Chip"
    cookie_mod.cookie_quantity = "6"
    assert cookie_mod.cookie_quantity == "6"
    cookie_mod.price_per_dozen = "6.99"
    assert cookie_mod.price_per_dozen == "6.99"
    # modifying attribute values for non-default values
    cookie_mod2 = new_Cookie()
    cookie_mod2.name = "Oreo"
    assert cookie_mod2.name == "Oreo"
    cookie_mod2.cookie_quantity = "8"
    assert cookie_mod2.cookie_quantity == "8"
    cookie_mod2.price_per_dozen = "10"
    assert cookie_mod2.price_per_dozen == "10"


def test_IceCream():
    # testing constructor for default values
    ice_cream = IceCream()
    assert ice_cream.name == ""
    assert ice_cream.scoop_count == 0
    assert ice_cream.price_per_scoop == 0
    # testing constructor for non-default values
    assert new_IceCream().name == "test ice cream"
    assert new_IceCream().scoop_count == 3
    assert new_IceCream().price_per_scoop == 1.99
    # modifying attribute values for default values
    ice_cream_mod = IceCream()
    ice_cream_mod.name = "Chocolate Chip"
    assert ice_cream_mod.name == "Chocolate Chip"
    ice_cream_mod.scoop_count = "6"
    assert ice_cream_mod.scoop_count == "6"
    ice_cream_mod.price_per_scoop = "6.99"
    assert ice_cream_mod.price_per_scoop == "6.99"
    # modifying attribute values for non-default values
    ice_cream_mod2 = new_IceCream()
    ice_cream_mod2.name = "Vanilla"
    assert ice_cream_mod2.name == "Vanilla"
    ice_cream_mod2.scoop_count = "8"
    assert ice_cream_mod2.scoop_count == "8"
    ice_cream_mod2.price_per_scoop = "10"
    assert ice_cream_mod2.price_per_scoop == "10"


def test_Sundae():
    # testing constructor for default values
    sundae = Sundae()
    assert sundae.name == ""
    assert sundae.scoop_count == 0
    assert ice_cream.price_per_scoop == 0
    # testing constructor for non-default values
    assert new_IceCream().name == "test ice cream"
    assert new_IceCream().scoop_count == 3
    assert new_IceCream().price_per_scoop == 1.99
    # modifying attribute values for default values
    ice_cream_mod = IceCream()
    ice_cream_mod.name = "Chocolate Chip"
    assert ice_cream_mod.name == "Chocolate Chip"
    ice_cream_mod.scoop_count = "6"
    assert ice_cream_mod.scoop_count == "6"
    ice_cream_mod.price_per_scoop = "6.99"
    assert ice_cream_mod.price_per_scoop == "6.99"
    # modifying attribute values for non-default values
    ice_cream_mod2 = new_IceCream()
    ice_cream_mod2.name = "Vanilla"
    assert ice_cream_mod2.name == "Vanilla"
    ice_cream_mod2.scoop_count = "8"
    assert ice_cream_mod2.scoop_count == "8"
    ice_cream_mod2.price_per_scoop = "10"
    assert ice_cream_mod2.price_per_scoop == "10"
