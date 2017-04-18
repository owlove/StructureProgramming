a = int(input("write a: "))
b = int(input("write b: "))
c = int(input("write c: "))

if((a < b + c) and (b < a + c) and (c < a + b)):
    print("You can build a triangle!")
else: print("Can not build a triangle!")