import random


class Dog:
    def __init__(self, name):
        self.name = name
        self.gladness = 50
        self.height = 20
        self.alive = True

    def eating(self):
        print('Time to study')
        self.gladness += 3
        self.height += 0.25


    def to_sleep(self):
        print("I will sleep")
        self.gladness += 3
        self.height -= 0.10
    def to_chill(self):
        print("Rest time")
        self.gladness += 5
        self.height -= 0.1

    def is_alive(self):
        if self.height < 7:
            print("Lack of weight...")
            self.alive = False
        elif self.gladness <= 0:
            print("Depression...")
            self.alive = False
        elif self.height > 45:
            print("Obesity...")
            self.alive = False

    def end_of_day(self):
        print(f"Gladness = {self.gladness}")
        print(f"Height = {round(self.height, 1)}")

    def live(self, day):
        d = "Day" + str(day) + " of " + self.name + " life"
        print(f"{day:=^50}")
        live_cube = random.randint(1, 3)
        if live_cube == 1:
            self.eating()
        elif live_cube == 2:
            self.to_sleep()
        elif live_cube == 3:
            self.to_chill()
        self.end_of_day()
        self.is_alive()


name = input("Input name ")
nick = Dog(name=name)
for i in range(1, 365):
    if nick.alive == False:
        break
    nick.live(i)