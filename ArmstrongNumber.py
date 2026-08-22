num = int(input("Enter the number : "))
sum = 0

temp = num
while temp > 0:
    digit = temp % 10
    sum = sum + (digit**3)
    temp = temp // 10

print ("Sum :", sum)
if(sum == num):
    print("This is an Armstrong number.")
else:
    print("This is not an Armstrong number")