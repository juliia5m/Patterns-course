from contr import Controller1
from device_tv import TV
from device_radio import Radio


def main():
    tv = TV()
    radio = Radio()

    controller_tv = Controller1(goal=tv)
    controller_radio = Controller1(goal=radio)

    controller_universal = Controller1(goal=[tv, radio])

    controller_tv.device_on()
    for i in range(3):
        controller_tv.device_next_channel()

    controller_tv.device_vol_down()

    controller_radio.device_on()

    for i in range(3):
        controller_radio.device_vol_down()
    controller_radio.device_next_channel()

    controller_universal.device_off()


if __name__ == '__main__':
    main()
