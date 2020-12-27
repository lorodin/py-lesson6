# 1. Создать класс TrafficLight (светофор) и определить у него один атрибут color (цвет) и метод running (запуск).
# Атрибут реализовать как приватный.
# В рамках метода реализовать переключение светофора в режимы: красный, желтый, зеленый.
# Продолжительность первого состояния (красный) составляет 7 секунд, второго (желтый) — 2 секунды,
# третьего (зеленый) — на ваше усмотрение.
# Переключение между режимами должно осуществляться только в указанном порядке (красный, желтый, зеленый).
# Проверить работу примера, создав экземпляр и вызвав описанный метод.
# Задачу можно усложнить, реализовав проверку порядка режимов, и при его нарушении выводить
# соответствующее сообщение и завершать скрипт.

from time import sleep


class TrafficLight:
    __dt_colors = (7, 3, 5)
    __color_names = ('red', 'yellow', 'green')
    __running: bool
    color: int

    def __init__(self):
        self.color = 0
        self.__running = False

    def running(self, on_switch: lambda color: True):
        while on_switch(self.__color_names[self.color]):
            sleep(self.__dt_colors[self.color])
            self.color = (self.color + 1) % 3


def start_app():
    colors_queue = ['red', 'yellow', 'green', 'red', 'yellow', 'green']

    def on_switch_color(color):
        next_color = colors_queue.pop(0)
        if color != next_color:
            print(f"Error: Current color is {color}, but must be {next_color}")
            return False
        print(f"Switch color to '{color}'")
        return len(colors_queue) != 0

    traffic_light = TrafficLight()

    traffic_light.running(on_switch_color)


if __name__ == '__main__':
    start_app()
