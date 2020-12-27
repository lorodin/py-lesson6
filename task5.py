# 5. Создайте экземпляры классов, передайте значения атрибутов.
# Выполните доступ к атрибутам, выведите результат. Выполните вызов методов и также покажите результат.

from task4 import TownCar, SportCar, PoliceCar, WorkCar


cars = (TownCar(200, 'red'), SportCar(300, 'blue'), PoliceCar(280), WorkCar(30, 'green'))

for car in cars:
    print(f'Car name: {car.name}, car color: {car.color}, is police: {car.is_police}')

    car.go()

    car.show_speed()

    car.stop()

    print('----------------------------------------')
