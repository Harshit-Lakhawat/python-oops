class student:

    year = 2024
    num_student = 0

    def __init__(self,name,age):
        self.name = name
        self.age = age
        student.num_student += 1 #modifying the class variable
        # so instead of self we use class name


student1 = student("abc",22)
student2 = student("harshit",18)
student3 = student("harsh",8)
student4 = student("har",1)

print(f"my graduating class of {student.year} has {student.num_student} students")
print(student1.name)
print(student2.name)
print(student3.name)
print(student4.name)
