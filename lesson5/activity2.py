def find_factorial(n):
    print(n)
    if n <= 0:
        return 1
    return n * find_factorial(n-1)


num = int(input("Enter the number: "))
print("Factorial:", find_factorial(num))

#5! = 5*4*3*2*1 = 120