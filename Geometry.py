def perimeterC(r):
    return 2*3.14*r
def perimeterS(s):
    return s*4

print("1. Perimeter of Cicle")
print("2. Perimeter of Square")

ch = int(input("Enter choice : "))

if ch == 1:
    r = int(input("What is the radius : "))
    print("The perimeter of this circle is", perimeterC(r))
elif ch == 2:
    s = int(input("What is the lenght of the sides : "))
    print("The perimeter of this sqaure is", perimeterS(s))
