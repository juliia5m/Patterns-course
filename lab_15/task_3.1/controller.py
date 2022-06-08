
class Controller:
    def __init__(self, on_, off_):
        self.on_ = on_
        self.off_ = off_

    def on(self):
        self.on_.do()

    def off(self):
        self.off_.do()