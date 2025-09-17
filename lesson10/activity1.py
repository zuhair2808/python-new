class Employee:

    def __init__(self):
        print("Employee is created.")

    def __del__(self):
        print("Employee is deleted.")

emp1 = Employee()
del emp1
