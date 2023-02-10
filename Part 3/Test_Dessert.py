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
    assert candy.price == 0
    # testing constructor for non-default values
    assert new_Candy().name == "test candy"
    assert new_Candy().candy_weight == 2.56
    assert new_Candy().price == 1.50
    # modifying attribute values for default values
    candy_mod = Candy()
    candy_mod.name = "Sweettarts"
    assert candy_mod.name == "Sweettarts"
    candy_mod.candy_weight = "2.9"
    assert candy_mod.candy_weight == "2.9"
    candy_mod.price = "1"
    assert candy_mod.price == "1"
    # modifying attribute values for non-default values
    candy_mod2 = new_Candy()
    candy_mod2.name = "Twix"
    assert candy_mod2.name == "Twix"
    candy_mod2.candy_weight = "3"
    assert candy_mod2.candy_weight == "3"
    candy_mod2.price = "100"
    assert candy_mod2.price == "100"


def test_Cookie():
    # testing constructor for default values
    cookie = Cookie()
    assert cookie.name == ""
    assert cookie.cookie_quantity == 0
    assert cookie.price == 0
    # testing constructor for non-default values
    assert new_Cookie().name == "test cookie"
    assert new_Cookie().cookie_quantity == 12
    assert new_Cookie().price == 12.99
    # modifying attribute values for default values
    cookie_mod = Cookie()
    cookie_mod.name = "Chocolate Chip"
    assert cookie_mod.name == "Chocolate Chip"
    cookie_mod.cookie_quantity = "6"
    assert cookie_mod.cookie_quantity == "6"
    cookie_mod.price = "6.99"
    assert cookie_mod.price == "6.99"
    # modifying attribute values for non-default values
    cookie_mod2 = new_Cookie()
    cookie_mod2.name = "Oreo"
    assert cookie_mod2.name == "Oreo"
    cookie_mod2.cookie_quantity = "8"
    assert cookie_mod2.cookie_quantity == "8"
    cookie_mod2.price = "10"
    assert cookie_mod2.price == "10"


def test_IceCream():
    # testing constructor for default values
    ice_cream = IceCream()
    assert ice_cream.name == ""
    assert ice_cream.scoop == 0
    assert ice_cream.price == 0
    # testing constructor for non-default values
    assert new_IceCream().name == "test ice cream"
    assert new_IceCream().scoop == 3
    assert new_IceCream().price == 1.99
    # modifying attribute values for default values
    ice_cream_mod = IceCream()
    ice_cream_mod.name = "Chocolate Chip"
    assert ice_cream_mod.name == "Chocolate Chip"
    ice_cream_mod.scoop = "6"
    assert ice_cream_mod.scoop == "6"
    ice_cream_mod.price = "6.99"
    assert ice_cream_mod.price == "6.99"
    # modifying attribute values for non-default values
    ice_cream_mod2 = new_IceCream()
    ice_cream_mod2.name = "Vanilla"
    assert ice_cream_mod2.name == "Vanilla"
    ice_cream_mod2.scoop = "8"
    assert ice_cream_mod2.scoop == "8"
    ice_cream_mod2.price = "10"
    assert ice_cream_mod2.price == "10"


def test_Sundae():
    # testing constructor for default values
    sundae = Sundae()
    assert sundae.name == ""
    assert sundae.scoop == 0
    assert sundae.price == 0
    assert sundae.topping_name == ""
    assert sundae.topping_price == ""
    # testing constructor for non-default values
    assert new_Sundae().name == "test sundae"
    assert new_Sundae().scoop == 3
    assert new_Sundae().price == .69
    assert new_Sundae().topping_name == "test topping"
    assert new_Sundae().topping_price == 1.29
    # modifying attribute values for default values
    sundae_mod = Sundae()
    sundae_mod.name = "Chocolate"
    assert sundae_mod.name == "Chocolate"
    sundae_mod.scoop = "6"
    assert sundae_mod.scoop == "6"
    sundae_mod.price = "6.99"
    assert sundae_mod.price == "6.99"
    sundae_mod.topping_name = "Hot Fudge"
    assert sundae_mod.topping_name == "Hot Fudge"
    sundae_mod.topping_price = "1.99"
    assert sundae_mod.topping_price == "1.99"
    # modifying attribute values for non-default values
    sundae_mod2 = new_Sundae()
    sundae_mod2.name = "Vanilla"
    assert sundae_mod2.name == "Vanilla"
    sundae_mod2.scoop = "8"
    assert sundae_mod2.scoop == "8"
    sundae_mod2.price = "10"
    assert sundae_mod2.price == "10"
    sundae_mod2.topping_name = "Hot Fudge"
    assert sundae_mod2.topping_name == "Hot Fudge"
    sundae_mod2.topping_price = "1.99"
    assert sundae_mod2.topping_price == "1.99"
