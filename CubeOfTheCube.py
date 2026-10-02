def Cube_Number(Num):
    return Num**3
def Checking(Num):
    if Num%3 == 0:
        return Cube_Number(Num)
    else:
        return False 
print (Checking(9))
print (Checking(5))
