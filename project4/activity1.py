sum = 0

num = int(input("Enter the number:"))

originalnum = num

while num > 0:
    digit = num % 10
    sum = sum + (digit ** 3)
    num = num//10

if originalnum == sum:
    print(originalnum, "Is an armstrong number")
else: print(originalnum, "Is not an armstrong number")