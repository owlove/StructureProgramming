import math
print("write koordinati tochki x and y ")
x = float(input("write x: "))
y = float(input("write y: "))

print("write r and R")
r = float(input("write r: "))
R = float(input("write R: "))

a =  math.sqrt(x**2 + y**2)
if (a > R) and (a < r):
    print("ne prenadlizhit")
else: print("prenadlezhit")