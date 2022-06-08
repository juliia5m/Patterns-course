from operator import Operator
from runway import Runway
from plane import Plane


def main():
    r1 = Runway(id=1)
    r2 = Runway(id=2)

    plane1 = Plane(plane_id="i1", runway_id=r1.get_id())
    plane2 = Plane(plane_id="i2", runway_id=r2.get_id())

    operator = Operator()

    operator.new_plane(plane1)
    operator.new_plane(plane2)

    operator.new_runway(r1)
    operator.new_runway(r2)

    plane1.take_off()
    plane2.take_off()


if __name__ == '__main__':
    main()
