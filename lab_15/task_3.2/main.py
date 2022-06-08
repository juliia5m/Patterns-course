from contr import Contr
from lamp import Lamp


def main():

    bd_lamp = Lamp('Bedroom')
    bath_lamp = Lamp('Bathroom')

    controller_bedroom_lamp = Contr(goal=bd_lamp)
    controller_bathroom_lamp = Contr(goal=bath_lamp)

    controller_universal = Contr(goal=[bd_lamp, bath_lamp])

    controller_bedroom_lamp.on()
    controller_bedroom_lamp.off()

    controller_bedroom_lamp.on()
    controller_bathroom_lamp.on()

    controller_universal.off()


if __name__ == '__main__':
    main()
