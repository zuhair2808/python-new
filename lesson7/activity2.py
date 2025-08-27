person = {
    "name": "Zuhair",
    "Age": "12",
    "profession": "student"
}
print("Person:", person)
print("Name:", person["name"])
print("Age:", person.get("age"))
person["city"] = "New York"
print("Updated:", person)
person.pop("profession")
print("Updated:", person)
person.clear()
print("After clearing:", person)