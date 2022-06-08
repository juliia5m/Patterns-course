from abc import ABC, abstractmethod


class Device(ABC):
    @abstractmethod
    def on(self):
        pass

    @abstractmethod
    def off(self):
        pass

    @abstractmethod
    def vol_up(self):
        pass

    @abstractmethod
    def vol_down(self):
        pass

    @abstractmethod
    def next_channel(self):
        pass

    @abstractmethod
    def prev_channel(self):
        pass





