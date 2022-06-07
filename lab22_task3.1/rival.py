from abc import ABC, abstractmethod


class Rival(ABC):
    def defend(self):
        self.pick_up_weapon()
        self.defense_action()
        self.move_to_safety()
        print()
        print('---------')

    @abstractmethod
    def pick_up_weapon(self):
        pass

    @abstractmethod
    def defense_action(self):
        pass

    @abstractmethod
    def move_to_safety(self):
        pass




