string = input("Enter the statement : ")

for i in string:
    if i == "A" or i == "a":
        print("A/a is visible")
        break
    else:
        print("Not found")