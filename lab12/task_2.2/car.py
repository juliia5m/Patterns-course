
class Car:
    def __init__(self, model, color, engine, wheel):
        self._model = model
        self._color = color
        self._engine = engine
        self._wheel = wheel

    def info(self):
        print( f'model : {self._model}', f'wheel : {self._wheel}', f'engine : {self._engine}', f'color : {self._color}')