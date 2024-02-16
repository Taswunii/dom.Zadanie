class Car:
    height = 2200
    satiety = 80
    hp = 220

class Sportcar(Car):
    height = 2050
    satiety = 90
    hp = 350
    grap = 70

class Hypercar(Sportcar):
    height = 1750
    satiety = 100
    hp = 800
    grap = 95
    aerodynamics = 100
    def __init__(self):
        print(self.height)
        print(self.satiety)
        print(self.hp)
        print(self.grap)
        print(self.aerodynamics)

ch = Hypercar()
