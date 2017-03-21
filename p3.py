a = int(input("Write first side: "))
b = int(input("Write second side: "))
c = int(input("Write third side: "))
if (a + b > c) and (a + c > b) and (b + c > a):
    print("Tringle can be")
else: print("This is not tringle")