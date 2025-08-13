number = int(input("Enter the number: "))

if number > 50:
    print(number, "is greater then 50", end=" ")
    if number %2 == 0:
        print ("and its even.")
    else:
        print ("and its odd.")
else:
    print(number,"is not greater then 50.")