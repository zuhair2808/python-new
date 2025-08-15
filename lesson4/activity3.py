num = int(input("Enter the number until which you want to find the sum of natural numbers: "))

i = 1
sum = 0

while i<= num:
    sum = sum + i
    i = i + 1
print("Sum:", sum)