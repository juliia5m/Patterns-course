from rival import Rival


class Pirate(Rival):

    def pick_up_weapon(self):
        print('Pick up sword')

    def defense_action(self):
        print('Defend with sword')

    def move_to_safety(self):
        print('Return to the ship')