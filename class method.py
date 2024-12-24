class Student :

    count = 0
    total_gpa = 0

    def __init__(self,name,gpa):
        self.name = name
        self.gpa = gpa
        Student.count += 1
        Student.total_gpa += gpa

    #instance method
    def get_info(self):
        return f"{self.name} {self.gpa}"

    @classmethod
    def get_count(cls):
        return f"Total no. of students: {cls.count}"
    @classmethod
    def get_average_gpa(cls):
       if cls.count == 0:
           return 0
       else:
           return f"Average gpa: {cls.total_gpa/cls.count:.2f}"



student1 = Student("harshit",9)
student2 = Student("hars",8)
student3 = Student("har",9)

print(Student.get_count())
print(Student.get_average_gpa())