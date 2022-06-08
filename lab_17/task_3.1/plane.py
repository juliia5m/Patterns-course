class Plane:
    def __init__(self, plane_id, runway_id):
        self._in_the_air = False
        self._id = plane_id
        self._runway_id = runway_id
        self._airport_operator = None

    def take_off(self):
        self._airport_operator.take_off(self._id, self._runway_id)

    def set_in_the_air(self, in_the_air):
        self._in_the_air = in_the_air

    def whether_in_the_air(self):
        return self._in_the_air

    def get_id(self):
        return self._id

    def get_runway_id(self):
        return self._runway_id

    def set_operator(self, operator):
        self._airport_operator = operator


