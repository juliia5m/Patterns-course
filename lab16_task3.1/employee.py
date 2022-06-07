class Employee:
    def __init__(self, name, position, age):
        self._name = name
        self._position = position
        self._age = age

    def get_name(self):
        return self._name

    def get_position(self):
        return self._position

    def get_age(self):
        return self._age
