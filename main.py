class Car:
    mark = "Audi"
    model = "gt rs"
    year = "2023"

    def __init__(self):
        self.name = "E-tron"
        self.hp = 600


cr = Car()

print(cr.mark, cr.name, cr.model, cr.hp, "hp")



class Animal:
    group = "mammal"
    tipe = "predator"
    eats = "omnivorous"

    def __init__(self):
        self.name = "lion"
        self.height = 190


an = Animal()

print(an.group, an.tipe, an.eats, an.name, an.height, "kg")

