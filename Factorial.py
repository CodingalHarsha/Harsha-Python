def Factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * Factorial(n-1)

print("The Factorial of 1 is : ", Factorial(1))
print("The Factorial of 2 is : ", Factorial(2))
print("The Factorial of 3 is : ", Factorial(3))
print("The Factorial of 4 is : ", Factorial(4))
print("The Factorial of 5 is : ", Factorial(5))
print("The Factorial of 6 is : ", Factorial(6))