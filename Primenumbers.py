lowerRange = int(input("Enter the lower range : "))
upperRange = int(input("Enter the upper range : "))

for i in range(lowerRange, upperRange + 1):
    if i > 1:
        for j in range (2,i):
            if i%j == 0:
                break
        else:
            print(i)