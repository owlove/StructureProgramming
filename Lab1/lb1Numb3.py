import math
x = float(input("Write number (x): "))
y = float(input("Write number (y): "))
t = float(input("Write number (t): "))

p = (math.pow(math.sin(x),3) + math.log1p(2 * y +  3 * x)/(math.pow(t,math.e)))
print(p)