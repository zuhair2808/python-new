weight = float(input("Enter weight in kg: "))
height = float(input("Enter height in meters: "))

bmi = weight / (height * height)

print("BMI:", bmi)

if bmi < 18.5:
    print ("Underweight")
elif bmi >= 18.5 and bmi <= 24.9:
    print("Healthy")
elif bmi >= 24.9 and bmi <= 29.9:
    print("Overweight")
elif bmi >= 30:
    print("Obese")
else:
    print("Something went wrong!")