class H_br:
    def __init__(self):
        self._is_up = False

    def push_down(self):
        self._is_up = False
        print('handbrake down')

    def lift_up(self):
        self._is_up = False
        print('handbrake lift up')