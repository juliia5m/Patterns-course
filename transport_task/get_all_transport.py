from trans_factory import SkodaFactory, VolvoFactory


def get_factory(car_name):
    if car_name == "Skoda":
        fact = SkodaFactory()
    elif car_name == "Volvo":
        fact = VolvoFactory()
    else:
        return 'we don"t have a factory for this car'
    return fact


def get_calculations(fact, n_buses, n_trams, n_trolleybuses, N):
    buses = []
    trams = []
    trolley = []

    for i in range(n_buses):
        buses.append(fact.create_bus())

    for i in range(n_trams):
        trams.append(fact.create_tram())

    for i in range(n_trolleybuses):
        trolley.append(fact.create_trolleybus())

    buses_res = []
    trams_res = []
    trolley_res = []

    for b in buses:
        buses_res.append(b.get_cost() + b.get_cost_of_usage() * N)

    for t in trams:
        trams_res.append(t.get_cost() + t.get_cost_of_usage() * N)

    for tr in trolley:
        trolley_res.append(tr.get_cost() + tr.get_cost_of_usage() * N)

    return sum(buses_res) + sum(trams_res) + sum(trolley_res)


print(get_calculations(get_factory("Volvo"), 10, 5, 40, 200000))  # same as in class
print(get_calculations(get_factory("Skoda"), 10, 5, 40, 200000))  # same as in class
