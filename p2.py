a = int(input("Write first number: "))
b = int(input("Write second number: "))
c = int(input("Write third number: "))
if a > b and a > c:
    print("max: ", a)
elif b > a and b > c:
    print("max: ", b)
else: print("max: ", c)