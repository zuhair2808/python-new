class Student:

    grade = 10

    def __init__(self, name, id, age):

        self.name = name
        self.id = id
        self.age = age

    def display(self):
        print("📖 Student Profile")
        print("Name", self.name)
        print("Grade", self.grade)
        print("ID", self.id)
        print("Age", self.age)
        print()

ripley = Student("Ripley", 4423, 20)
ripley.display()

ellen = Student("Ellen", 5233, 17)
ellen.display()