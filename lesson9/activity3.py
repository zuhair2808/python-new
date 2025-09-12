class Parrot:
    type = "Bird"
    def __init__(self, name, age):
        self.name = name
        self.age = age
woo = Parrot("Woo", 2)
print(f"Species: {woo.type}, Name: {woo.name}, Age: {woo.age}")

blu = Parrot("Blu", 3)
print(f"Species: {blu.type}, Name: {blu.name}, Age: {blu.age}")