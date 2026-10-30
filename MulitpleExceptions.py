try:
    num1 = int(input("Enter number 1 : "))
    num2 = int(input("Enter number 2 : "))
    print("Division : ", num1/num2)
except ValueError as ex:
    print("Value Error expection handeled ")
except ZeroDivisionError as ex:
    print("Zero Division Error exception handeled")
else:
    print("No exceptions occured")
finally:
    print("Will execute at any cost")
