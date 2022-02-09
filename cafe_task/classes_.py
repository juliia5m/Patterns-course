from beverage import Beverage


class Americano(Beverage):

    def __init__(self):
        super().__init__(5, 25)

    def taste(self):
        return "a very tasty beverage"


class Cappuccino(Beverage):

    def __init__(self):
        super().__init__(10, 50)

    def taste(self):
        return "a very tasty beverage"


class Expresso(Beverage):

    def __init__(self):
        super().__init__(3, 30)

    def taste(self):
        return "a very tasty beverage"


class Late(Beverage):

    def __init__(self):
        super().__init__(4, 54)

    def taste(self):
        return "my favourite beverage"

class Tea(Beverage):

    def __init__(self):
        super().__init__(2, 20)

    def taste(self):
        return "a very tasty beverage"

