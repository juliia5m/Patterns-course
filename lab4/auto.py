# as in class

class Auto:
    def __init__(self, age, model, damaged, kilometrage):
        self.age = age
        self.model = model
        self.damaged = damaged
        self.kilometrage = kilometrage

    def __str__(self):
        return f'result(how_old={self.age}years, model={self.model}, whether_damaged={self.damaged}, kilometrage={self.kilometrage})'
