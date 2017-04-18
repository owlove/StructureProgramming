a = int(input("write a: "))
b = int(input("write b: "))
c = int(input("write c: "))
d = int(input("write d: "))

if (a % 2 == 0) and (b % 2 ==0) and (c % 2 != 0) and (d % 2 != 0):
    print("True")
elif(a % 2 == 0) and (b % 2 !=0) and (c % 2 == 0) and (d % 2 != 0):
    print("True")
elif(a % 2 == 0) and (b % 2 !=0) and (c % 2 != 0) and (d % 2 == 0):
    print("True")
elif(a % 2 != 0) and (b % 2 ==0) and (c % 2 == 0) and (d % 2 != 0):
    print("True")
elif(a % 2 != 0) and (b % 2 ==0) and (c % 2 != 0) and (d % 2 == 0):
    print("True")
elif(a % 2 != 0) and (b % 2 !=0) and (c % 2 == 0) and (d % 2 == 0):
    print("True")
else: print("False")