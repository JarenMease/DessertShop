import dessert

Candy = dessert.Candy
Cookie = dessert.Cookie
IceCream = dessert.IceCream
Sundae = dessert.Sundae


def new_Candy():
    return Candy("test candy",1.50, 2.56)


def new_Cookie():
    return Cookie("test cookie", 12, 12.99)


def new_IceCream():
    return IceCream("test ice cream", 3, 1.99)


def new_Sundae():
    return Sundae("test sundae", 3, 1.59, "test topping", .59)


def test_Candy():
    # testing constructor for default values
    candy = Candy()
    assert candy.name == ""
    assert candy.candy_weight == float
    assert candy.price == float
    assert candy.tax_percent == 7.25
    # testing constructor for non-default values
    assert new_Candy().name == "test candy"
    assert new_Candy().price == 1.50
    assert new_Candy().candy_weight == 2.56
    assert new_Candy().calculate_cost() == 3.84
    assert new_Candy().tax_percent == 7.25
    assert new_Candy().calculate_tax() == .2784
    # modifying attribute values for default values
    candy_mod = Candy()
    candy_mod.name = "Sweettarts"
    assert candy_mod.name == "Sweettarts"
    candy_mod.candy_weight = "2.9"
    assert candy_mod.candy_weight == "2.9"
    candy_mod.price = "1"
    assert candy_mod.price == "1"
    candy_mod.calculate_cost() == "2.9"
    assert candy_mod.calculate_cost() == 2.9
    candy_mod.tax_percent == "7.25"
    assert candy_mod.tax_percent == 7.25
    candy_mod.calculate_tax() == "0.21025"
    assert candy_mod.calculate_tax() == 0.21025
    # modifying attribute values for non-default values
    candy_mod2 = new_Candy()
    candy_mod2.name = "Twix"
    assert candy_mod2.name == "Twix"
    candy_mod2.candy_weight = "3"
    assert candy_mod2.candy_weight == "3"
    candy_mod2.price = "100"
    assert candy_mod2.price == "100"
    candy_mod2.calculate_cost() == "300"
    assert candy_mod2.calculate_cost() == 300
    candy_mod2.tax_percent == "7.25"
    assert candy_mod2.tax_percent == 7.25
    candy_mod2.calculate_tax() == "21.75"
    assert candy_mod2.calculate_tax() == 21.75


def test_Cookie():
    # testing constructor for default values
    cookie = Cookie()
    assert cookie.name == " Cookies"
    assert cookie.cookie_quantity == int
    assert cookie.price == float
    assert cookie.tax_percent == 7.25
    # testing constructor for non-default values
    assert new_Cookie().name == "test cookie Cookies"
    assert new_Cookie().cookie_quantity == 12
    assert new_Cookie().price == 12.99
    assert new_Cookie().calculate_cost() == 12.99
    assert new_Cookie().tax_percent == 7.25
    assert new_Cookie().calculate_tax() == .9417749999999999
    # modifying attribute values for default values
    cookie_mod = Cookie()
    cookie_mod.name = "Chocolate Chip"
    assert cookie_mod.name == "Chocolate Chip"
    cookie_mod.cookie_quantity = "6"
    assert cookie_mod.cookie_quantity == "6"
    cookie_mod.price = "6.99"
    assert cookie_mod.price == "6.99"
    cookie_mod.calculate_cost() == "3.495"
    assert cookie_mod.calculate_cost() == 3.495
    cookie_mod.tax_percent == "7.25"
    assert cookie_mod.tax_percent == 7.25
    cookie_mod.calculate_tax() == ".2533875"
    assert cookie_mod.calculate_tax() == .2533875
    # modifying attribute values for non-default values
    cookie_mod2 = new_Cookie()
    cookie_mod2.name = "Oreo"
    assert cookie_mod2.name == "Oreo"
    cookie_mod2.cookie_quantity = "8"
    assert cookie_mod2.cookie_quantity == "8"
    cookie_mod2.price = "10"
    assert cookie_mod2.price == "10"
    cookie_mod2.calculate_cost() == "6.666666666666667"
    assert cookie_mod2.calculate_cost() == 6.666666666666667
    cookie_mod2.tax_percent == "7.25"
    assert cookie_mod2.tax_percent == 7.25
    cookie_mod2.calculate_tax() == "0.48333333333333334"
    assert cookie_mod2.calculate_tax() == 0.48333333333333334


def test_IceCream():
    # testing constructor for default values
    ice_cream = IceCream()
    assert ice_cream.name == " Ice Cream"
    assert ice_cream.scoop == float
    assert ice_cream.price == float
    assert ice_cream.tax_percent == 7.25
    # testing constructor for non-default values
    assert new_IceCream().name == "test ice cream Ice Cream"
    assert new_IceCream().scoop == 3
    assert new_IceCream().price == 1.99
    assert new_IceCream().calculate_cost() == 5.97
    assert new_IceCream().tax_percent == 7.25
    assert new_IceCream().calculate_tax() == 0.43282499999999996
    # modifying attribute values for default values
    ice_cream_mod = IceCream()
    ice_cream_mod.name = "Chocolate Chip"
    assert ice_cream_mod.name == "Chocolate Chip"
    ice_cream_mod.scoop = "6"
    assert ice_cream_mod.scoop == "6"
    ice_cream_mod.price = "6.99"
    assert ice_cream_mod.price == "6.99"
    ice_cream_mod.calculate_cost() == "41.94"
    assert ice_cream_mod.calculate_cost() == 41.94
    ice_cream_mod.tax_percent == "7.25"
    assert ice_cream_mod.tax_percent == 7.25
    ice_cream_mod.calculate_tax() == "3.0406499999999994"
    assert ice_cream_mod.calculate_tax() == 3.0406499999999994
    # modifying attribute values for non-default values
    ice_cream_mod2 = new_IceCream()
    ice_cream_mod2.name = "Vanilla"
    assert ice_cream_mod2.name == "Vanilla"
    ice_cream_mod2.scoop = "8"
    assert ice_cream_mod2.scoop == "8"
    ice_cream_mod2.price = "10"
    assert ice_cream_mod2.price == "10"
    ice_cream_mod2.calculate_cost() == "80.0"
    assert ice_cream_mod2.calculate_cost() == 80.0
    ice_cream_mod2.tax_percent == "7.25"
    assert ice_cream_mod2.tax_percent == 7.25
    ice_cream_mod2.calculate_tax() == "5.8 "
    assert ice_cream_mod2.calculate_tax() == 5.8


def test_Sundae():
    # testing constructor for default values
    sundae = Sundae()
    assert sundae.name == "  Sundae Ice Cream"
    assert sundae.scoop == float
    assert sundae.price == float
    assert sundae.topping_name == ""
    assert sundae.topping_price == float
    # assert sundae.calculate_cost() == ""
    assert sundae.tax_percent == 7.25
    # assert sundae.calculate_tax() == ""
    # testing constructor for non-default values
    assert new_Sundae().name == "test topping test sundae Sundae Ice Cream"
    assert new_Sundae().scoop == 3
    assert new_Sundae().price == 1.59
    assert new_Sundae().topping_name == "test topping"
    assert new_Sundae().topping_price == .59
    assert new_Sundae().calculate_cost() == 5.36
    assert new_Sundae().tax_percent == 7.25
    assert new_Sundae().calculate_tax() == 0.3886
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
    sundae_mod.calculate_cost() == "43.93"
    assert sundae_mod.calculate_cost() == 43.93
    sundae_mod.tax_percent == "7.25"
    assert sundae_mod.tax_percent == 7.25
    sundae_mod.calculate_tax() == "3.184925"
    assert sundae_mod.calculate_tax() == 3.184925
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
    sundae_mod2.calculate_cost() == "81.99"
    assert sundae_mod2.calculate_cost() == 81.99
    sundae_mod2.tax_percent == "7.25"
    assert sundae_mod2.tax_percent == 7.25
    sundae_mod2.calculate_tax() == "5.944274999999999 "
    assert sundae_mod2.calculate_tax() == 5.944274999999999


def test_dessert_item():
    candy = Candy("SweetRopes", 1.20, 2.30)
    assert candy.name == "SweetRopes"
    assert candy.candy_weight == 2.30
    assert candy.price == 1.20
    assert candy.calculate_cost() == 2.76
    assert candy.tax_percent == 7.25
    assert candy.calculate_tax() == .20009999999999997
