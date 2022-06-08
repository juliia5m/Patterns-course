class Runway:
    def __init__(self, id):
        self._is_available = True
        self._id = id

    def get_id(self):
        return self._id

    def is_available(self, is_available):
        self._is_available = is_available

    def whether_is_available(self):
        return self._is_available
