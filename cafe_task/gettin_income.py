from classes_ import *
from needed_factory import ExpressoFactory, AmericanoFactory, LateFactory, CappuccinoFactory, TeaFactory, BeverageFactory




def get_income(cases, n_capuch, n_americano, n_late, n_tea, n_espresso):
    capuch_ = []
    late_ = []
    esp_ = []
    am_ = []
    t_ = []
    for case in cases:
        if case == "Espresso":
            fact = ExpressoFactory()
            for i in range(n_espresso):
                esp_.append(fact.create_beverage())

        elif case == "Americano":
            fact = AmericanoFactory()
            for i in range(n_americano):
                am_.append(fact.create_beverage())
        elif case == "Late":
            fact = LateFactory()
            for i in range(n_late):
                late_.append(fact.create_beverage())

        elif case == "Cappuccino":
            fact = CappuccinoFactory()

            for i in range(n_capuch):
                capuch_.append(fact.create_beverage())

        elif case == "Tea":
            fact = TeaFactory()
            for i in range(n_tea):
                t_.append(fact.create_beverage())

    capuch_res = []
    late_res = []
    esp_res = []
    am_res = []
    t_res = []

    for c in capuch_:

        capuch_res.append( - c.get_ingredients_cost() + c.get_sell_price())



    for c in late_:
        late_res.append( - c.get_ingredients_cost() + c.get_sell_price())


    for c in esp_:
        esp_res.append( - c.get_ingredients_cost() + c.get_sell_price())

    for c in am_:
        am_res.append( - c.get_ingredients_cost() + c.get_sell_price())

    for c in t_:
        t_res.append( - c.get_ingredients_cost() + c.get_sell_price())

    return sum(capuch_res) + sum(late_res) + sum(esp_res) + sum(am_res) + sum(t_res)




listt = ["Late", "Cappuccino", "Espresso", "Americano", "Tea"]

print(get_income(listt, 10, 10, 10, 5, 10))
