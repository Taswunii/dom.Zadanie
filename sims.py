import random


class Human:
    def __init__(self, name="Human", job=None, home=None, car=None):
        self.name = name
        self.money = 500
        self.gladness = 50
        self.satiety = 50
        self.job = job
        self.home = home
        self.car = car

    def get_home(self):
        self.home = House()
    def get_car(self):
        self.car = Auto(brand_of_car)
    def get_job(self):
        if self.car.drive():
            pass
        else:
            self.to_repair()
            return
        self.job = Job(job_list)
    def eat(self):
        if self.home.food <= 0:
            self.shopping("food")
        else:
            if self.satiety >= 100:
                self.satiety = 100
                return
            else:
                self.satiety += 5
                self.home.food -= 5
    def work(self):
        if self.car.drive():
            pass
        else:
            if self.car.fuel < 15:
                self.shopping("fuel")
                return
            else:
                self.to_repair()
                return
        self.money += self.job.salary
        self.gladness -= self.job.glagness
        self.satiety -= 5
    def shopping(self, manage):
        if self.car.drive():
            pass
        else:
            if self.car.fuel < 15:
                manage = "fuel"
            else:
                self.to_repair()
                return
            if manage == "fuel":
                print("I bought fuel!")
                self.money -= 25
                self.car.fuel += 100
            elif manage == "food":
                self.money -= 15
                self.home.food += 50
            elif manage == "delicacies":
                print("i`m happy")
                self.gladness += 20
                self.satiety += 2
                self.money -= 5
    def chill(self):
        print("Time to chill")
        self.gladness += 50
        self.home.mess += 15
    def clean_home(self):
        print("Cleaning time")
        self.gladness -= 10
        self.home.mess -= 100
    def to_repair(self):
        print("I`ll repair my car")
        self.car.straight += 100
        self.gladness -= 10
        self.money -= 15
    def days_indexes(self, day):
        d = f"Today the {day} of {self.name} life"
        print(f"{d:=^50}\n")
        
        h_i = f"{self.name}'s indexes"
        print(f"{h_i:=^50}\n")
        print(f"Money = {self.money}")
        print(f"Gladness = {self.gladness}")
        print(f"Sateity = {self.satiety}")

        home_i = "Home indexes"
        print(f"{home_i:=^50}\n")
        print(f"Food = {self.home.food}")
        print(f"Mess = {self.home.mess}")

        car_ind = f"{self.car.brand} car indexes"
        print(f"{car_ind:=^50}\n")
        print(f"Fuel = {self.car.fuel}")
        print(f"Straight = {self.car.straight}")
    def is_alive(self):
        if self.gladness < 0:
            print("Depression...")
            return False
        if self.satiety < 0:
            print("Dead...")
            return False
        if self.money < -100:
            print("Bankroupt...")
            return False

    def live(self, day):
        if self.is_alive() == False:
            return False
        if self.home is None:
            print("Sattled in the house")
            self.get_home()
        if self.car is None:
            self.get_car()
            print(f"I bought a car {self.car.brand}")
        if self.job is None:
            self.get_job()
            print(f"I work {self.job.job} and salary {self.job.salary}")
        self.days_indexes(day)
        dice = random.randint(1,4)
        if self.satiety < 20:
            print("Time to eat")
            self.eat()
        elif self.gladness < 20:
            print("Let`s chill")
            self.chill()
        elif self.money < 0:
            print("Start working")
            self.work()
        elif self.car.straight < 15:
            print("I need to repair my car")
            self.to_repair()
        elif dice == 1:
            print("Start working")
            self.work()
        elif dice == 3:
            print("Cleaning time")
            self.clean_home()
        elif dice == 4:
            print("Time to shopping")
            self.shopping(manage="delicacies")




class Auto:
    def __init__(self, brand_list):
        self.brand = random.choice(list(brand_list))
        self.fuel = brand_list[self.brand]["fuel"]
        self.straight = brand_list[self.brand]["straight"]
        self.cons = brand_list[self.brand]["cons"]


    def drive(self):
        if self.straight > 0 and self.fuel >= self.cons:
            self.fuel -= self.cons
            self.straight -= 1
            return True
        else:
            print("The car cannot move!")
            return False

class House:
    def __init__(self):
        self.food = 0
        self.mess = 0


class Job:
    def __init__(self, job_list):
        self.job = random.choice(list(job_list))
        self.salary = job_list[self.job]['salary']
        self.glagness = job_list[self.job]['gladness_less']














job_list = { "Java developer": {"salary":50, "gladness_less": 10 },
             "Python developer": {"salary":40, "gladness_less": 3 },
             "C++ developer": {"salary":45, "gladness_less": 25 },
             "Rust developer": {"salary":70, "gladness_less": 1 },}

brand_of_car ={"BMW" : {"fuel": 100, "straight": 100, "cons": 12},
                   "Lada": {"fuel": 100,"straight": 20, "cons": 10},
                   "Ferarri": {"fuel": 80,"straight": 120, "cons": 8},
                   "Volvo": {"fuel": 60,"straight": 80, "cons": 14}}


human = Human("Nick")
for i in range(1, 366):
    if human.live(i) == False:
        break





# h = Human()
# h.get_home()
# print(h.home.food)