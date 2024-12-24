class Animal:
    alive = True

class Dog(Animal):
    def speak(self):
        print("woof!!")

class Cat(Animal):
    def speak(self):
        print("meow!!")

class Car:
    #def horn(self): #error occur as car dont have speak attribute
        #print("honk!!")

    #animals = [Dog(),Cat(),Car()]
     #lets name horn as speak
    def speak(self): #no error as it has speak
        print("honk!!")
    alive = False
animals = [Dog(),Cat(),Car()]

for animal in animals:
    animal.speak()
    print(animal.alive)#error as car doesnot have alive attribute
    #then if we add alive = False it will work
