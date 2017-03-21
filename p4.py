a = int(input("Write first number a: "))
b = int(input("Write second number b: "))
c = int(input("Write third number c: "))
d = int(input("Write fourth number d: "))
for i in range (a, b):
    if (i % d == c):
        print("Number: ", i)