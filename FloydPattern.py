row = int(input("Enter the number of rows : "))

num = 1

for i in range (row):
    for i in range (i + 1):
            print(num,end=" ")
            num = num + 1
    print()