from commands import CommandOn, CommandOff
from controller import Controller
from lamp import Lamp


def main():
    lamp = Lamp()
    controller = Controller(CommandOn(lamp), CommandOff(lamp))

    controller.on()
    controller.on()
    controller.off()
    controller.on()


if __name__ == "__main__":
    main()