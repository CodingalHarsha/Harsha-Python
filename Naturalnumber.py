num = int(input("Enter your number until which you want to stop till : "))

sum = 0

i = 1

while i <= num:
    sum += i
    i += 1
print("Sum of all Natural number till", num, "is", sum)