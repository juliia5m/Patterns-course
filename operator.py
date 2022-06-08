
class Operator:
    def __init__(self):
        self._runways = {}
        self._on_ground = {}
        self._in_the_air = {}

    def new_plane(self, plane):
        assert plane.get_id() not in self._on_ground, " The Plane you chose is already registered"
        assert plane.get_id() not in self._in_the_air, "The Plane you chose is already registered"
        assert plane.get_runway_id() not in self._runways, "No such runway "

        self._on_ground[plane.get_id()] = plane
        plane.set_operator(self)

    def new_runway(self, runway):
        assert runway.get_id() not in self._runways, 'Runway you chose is already registered'

        self._runways[runway.get_id()] = runway

    def take_off(self, plane_id, runway_id):
        if plane_id in self._on_ground and self._runways[runway_id].whether_is_available():
            plane = self._on_ground.pop(plane_id)
            print(f'{plane_id} is taking off now. have a nice flight!')
            plane.set_in_the_air(True)
            self._runways[runway_id].is_available(False)
            plane.set_in_the_air(True)
            self._in_the_air[plane_id] = plane
        else:
            if plane_id not in self._on_ground:
                print(f'{plane_id} is already in the air.')
            if not self._runways[runway_id].whether_is_available():
                print(f'{runway_id} is not available.')