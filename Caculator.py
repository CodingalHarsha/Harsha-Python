def Add(num1,num2):
    return num1 + num2
def sub(num1,num2):
    return num1 - num2
def Mult(num1,num2):
    return num1 * num2
def Div(num1,num2):
    return num1 / num2

print('**************CALCULATOR***************')

print("1. Addition")
print("2. Subtraction")
print("3. Multiplication")
print("4. Division")

ch = int(input("Enter choice : "))
num1 = int(input("Enter number 1 : "))
num2 = int(input("Enter number 2 : "))

if ch == 1:
    print("Addition of ",num1," and ",num2,"=",Add(num1,num2))
elif ch == 2:
    print("Subtraction of ",num1," and ",num2,"=",sub(num1,num2))
elif ch == 3:
    print("Multiplication of ",num1," and ",num2,"=",Mult(num1,num2))
elif ch == 4:
    print("Division of ",num1," and ",num2,"=",Div(num1,num2))