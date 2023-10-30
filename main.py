import random
import pygame

list

i = random.randint()



class Car:

    color = "color"
    car_brand = "brand"

    def go(self):
        print("Go")

    def stop(self):
        print("Stop")

    def info(self):
        print(f"цвет машины: {self.color}, марка машины: {self.car_brand}")

car = Car()

print(car.color)
car.color = 'red'
print(car.color)
car.car_brand = 'bmw'
print(car.car_brand)

car.info()

car1 = Car()
car.color = "black"
car.car_brand = "mercedes"
car.info()

