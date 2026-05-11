class Student:
    count = 0
    total_gpa = 0

    def __init__(self,name,gpa):
        self.name = name
        self.gpa = gpa
        Student.count += 1
        Student.total_gpa += gpa
    #Instance Method
    def get_info(self):
        return f"{self.name} = {self.gpa}"

    @classmethod
    def get_count(cls):
        return f"Total # of students: {cls.count}"

    @classmethod
    def get_avg_gpa(cls):
        if cls.total_gpa == 0:
            return "No students to calculate average GPA"
        return f"Average GPA: {cls.total_gpa/Student.count}"

#student1 = Student("Jane Smith",3.1)
#student2 = Student("Jhony Smith",3.3)

print(Student.get_count())
print(Student.get_avg_gpa())