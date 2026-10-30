try:
    num1 = int(input("Enter number 1 :"))
    print("Number Entered : ", num1)
except ValueError as ex:
    print("Exception handeled ! ")


print("Line after try")