class animal:
    def __init__(self,name):
        self.name = name
    def eat(self):
        print(f"this {self.name} is eating")
    def sleep(self):
        print(f"this {self.name} is sleeping")
class prey(animal):
    def flee(self):
        print(f"{self.name} is preying")
class predator(animal):
    def hunt(self):
        print(f"this {self.name} is hunting")
class rabbit(prey):
    pass
class hawk(predator):
    pass
class fish(prey,predator):
    pass

rabbit = rabbit("bugs")
hawk = hawk("tony")
fish = fish("nemo")

rabbit.flee()
#rabbit.hunt() error as rabbit dont have hunt beacause
#it didnt call predator class

fish.flee()
fish.hunt()

fish.eat()

rabbit.eat()
