# 2. Реализовать класс Road (дорога), в котором определить атрибуты: length (длина), width (ширина).
# Значения данных атрибутов должны передаваться при создании экземпляра класса.
# Атрибуты сделать защищенными.
# Определить метод расчета массы асфальта, необходимого для покрытия всего дорожного полотна.
# Использовать формулу: длина*ширина*масса асфальта для покрытия одного кв метра дороги асфальтом,
# толщиной в 1 см*число см толщины полотна. Проверить работу метода.
# Например: 20м*5000м*25кг*5см = 12500 т

class Road:
    _length: int
    _width: int
    _density: int = 25
    _thick: int = 5

    def __init__(self, length, width):
        self._width = width
        self._length = length

    def calc_weight(self):
        result = self._width * self._length * self._density * self._thick
        if result > 1000:
            return f"{result / 1000}t"
        return f"{result}kg"


def start_app():
    road = Road(20, 5000)
    print(f"Road wight: {road.calc_weight()}")


if __name__ == "__main__":
    start_app()
