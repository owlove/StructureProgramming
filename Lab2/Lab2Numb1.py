x = int(input("write integer x: "))
y = int(input("write integer y: "))
z = int(input("write integer z: "))

if (x % 5 == 0) and (y % 5 != 0) and (z % 5 != 0 ):
    print("True")
elif (x % 5 != 0) and (y % 5 == 0) and (z % 5 != 0 ):
    print("True")
elif (x % 5 != 0) and (y % 5 != 0) and (z % 5 == 0 ):
    print("True")
else: print("False")