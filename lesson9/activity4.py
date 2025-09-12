class Parrot:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def info(self):
        print("Parrot Information:")
        print("Name:", self.name)
        print("Age:", self.age, "\n")

blu = Parrot("Blu", 3)
blu.info()

woo = Parrot("Woo", 2)
woo.info()
