class Employee:

    def __init__(self,name,position):
        self.name = name
        self.position = position
    def get_info(self):  #instance method
        return f"{self.name} = {self.position}"

    #each object that we create from this class will have there own get_info function

    @staticmethod
    def is_valid_position(position):
        valid_positions = ["manager","cashier","cook","janitor"]
        return position in valid_positions
employee1 = Employee("harshit","manager")
employee2 = Employee("harsh","cashier")
employee3 = Employee("ha","cook")

print(Employee.is_valid_position("cook")) #we donot make object as we call static method
print(employee1.get_info())
print(employee2.get_info())
print(employee3.get_info())
#for instance method we access an object then calls the instance method
#for static method we only need to access the class
