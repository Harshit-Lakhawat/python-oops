class animal:
    def __init__(self,name):
        self.name = name
        self.is_alive = True
    def eat(self):
        print(f"{self.name} is eating ")
    def sleep(self):
        print(f"{self.name} is sleeping ")
class dog(animal):
    def speak(self):
        print("woof!")
class cat(animal):
    def speak(self):
        print("meow!")

dog = dog("john")
cat = cat("sexy")

print(dog.name)
print(cat.name)
dog.eat()
cat.sleep()
dog.speak()
cat.speak()
