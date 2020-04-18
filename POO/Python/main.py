from car import Car
from account import Account

if __name__ == '__main__':
    car = Car("Placa", Account(122,"Pedro","F","@","contra"), 5)
    print(car.driver.id)

