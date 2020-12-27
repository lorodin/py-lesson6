# 6. Реализовать класс Stationery (канцелярская принадлежность).
# Определить в нем атрибут title (название) и метод draw (отрисовка).
# Метод выводит сообщение “Запуск отрисовки.”
# Создать три дочерних класса Pen (ручка), Pencil (карандаш), Handle (маркер).
# В каждом из классов реализовать переопределение метода draw.
# Для каждого из классов метод должен выводить уникальное сообщение.
# Создать экземпляры классов и проверить, что выведет описанный метод для каждого экземпляра.

class Stationary:
    title: str

    def draw(self):
        print('Run drawer')


class Pen(Stationary):
    def __init__(self):
        self.title = 'pen'

    def draw(self):
        print('Draw pen')


class Pencil(Stationary):
    def __init__(self):
        self.title = 'pencil'

    def draw(self):
        print('Draw pencil')


class Handle(Stationary):
    def __init__(self):
        self.title = 'handle'

    def draw(self):
        print('Handle draw')


tools = (Pen(), Pencil(), Handle())

for tool in tools:
    print(f'Tool name: {tool.title}')
    tool.draw()
    print('------------------------')
