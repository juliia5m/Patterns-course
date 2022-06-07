
class Staff:
    def __init__(self, employees):
        self._employees = employees
        self._i = None

    def __iter__(self):
        self._i = 0
        return self

    def __next__(self):
        N = len(self._employees)
        while self._i < N:
            employee = self._employees[self._i]
            self._i += 1
            return employee
        raise StopIteration
