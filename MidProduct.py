num = int(input("Enter your number:"))
temp = num
NumLen = 0

while temp > 0:
    NumLen = NumLen+1
    temp = int(temp/10)

if NumLen >=4:
    NumLen = int(NumLen/2)
    chk = 0
    while num >0:
        rem = num%10
        if chk == NumLen:
            midone = rem
        elif chk == (NumLen - 1):
            midtwo = rem

        num = int(num/10)
        chk= chk +1
    prod = midone*midtwo
    print("product of ", midone, "and", midtwo, "is", prod)
else:
    print("It's not 4 or more than 4 digit number.")
    