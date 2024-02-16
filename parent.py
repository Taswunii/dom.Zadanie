#class Grandparent:
#    height = 170
#   satiety = 100
#  age = 60
#
#class Parent(Grandparent):
 #   age = 40

#class Child(Parent):
#    height = 50
 #   age = 10
  #  def __init__(self):
   #     print(self.height)
    #    print(self.satiety)
     #   print(self.age)

#ch = Child()



class Hello_world:
    hello = "Hello"
    _hello = "_Hello"
    __hello = "__Hello"

    def __init__(self):
        self.world = "World"
        self._world = "_World"
        self.__world = "__World"
    def printer(self):
        print(self.hello)
        print(self._hello)
        print(self.__hello)
        print(self.world)
        print(self._world)
        print(self.__world)
class Hi(Hello_world):
    def hi_printer(self):
        print(self.hello)
        print(self._hello)
        print(self.__hello)
        print(self.world)
        print(self._world)
        print(self.__world)


h = Hello_world()
h.printer()
hi = Hi()
hi.hi_printer()



















