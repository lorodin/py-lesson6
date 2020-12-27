# 4.Реализуйте базовый класс Car.
# У данного класса должны быть следующие атрибуты: speed, color, name, is_police (булево).
# А также методы: go, stop, turn(direction), которые должны сообщать, что машина поехала,
# остановилась, повернула (куда).
# Опишите несколько дочерних классов: TownCar, SportCar, WorkCar, PoliceCar.
# Добавьте в базовый класс метод show_speed, который должен показывать текущую скорость автомобиля.
# Для классов TownCar и WorkCar переопределите метод show_speed.
# При значении скорости свыше 60 (TownCar) и 40 (WorkCar) должно выводиться сообщение о превышении скорости.

class Car:
    speed: int
    color: str
    name: str
    is_police: bool
    _is_go: bool
    __direction: str

    def __init__(self, speed, color, name, is_police = False):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police
        self._is_go = False

    def go(self):
        if self._is_go:
            print('Car already run')
        else:
            self._is_go = True
            print('Car started')

    def stop(self):
        if not self._is_go:
            print('Car already stop')
        else:
            self._is_go = False
            print('Car stopped')

    def turn(self, direction):
        if not self._is_go:
            print('Car is stopped')
        else:
            self.__direction = direction
            print(f'Car turn on {direction}')

    def show_speed(self):
        if not self._is_go:
            print('Car is stopped. Current speed is 0')
        else:
            print(f'Current speed: {self.speed}km/h')


class SlowCar(Car):
    _max_speed: int

    def show_speed(self):
        if not self._is_go:
            print('Car is stopped. Current speed is 0')
            return
        elif self.speed > self._max_speed:
            print('Warning. Exceeded maximum speed.')
        print(f'Current speed: {self.speed}km/h')


class TownCar(SlowCar):
    _max_speed = 60

    def __init__(self, speed, color):
        super().__init__(speed, color, 'TownCar')


class SportCar(Car):
    def __init__(self, speed, color):
        super().__init__(speed, color, 'SportCar')


class WorkCar(SlowCar):
    _max_speed = 40

    def __init__(self, speed, color):
        super().__init__(speed, color, 'WorkCar')


class PoliceCar(Car):
    def __init__(self, speed):
        super().__init__(speed, 'white-blue', 'PoliceCar', True)
