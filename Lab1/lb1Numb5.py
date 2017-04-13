import math
x = 8.5
c = int(input('введите (с): '))

b = x + c**2
print("b = ",b)
a = (math.fabs(b + c))**(1/3)
print("a = ",a)
y = math.pow(math.cos(b),2) + b * math.pow(math.cos(a**2),4)
print("y = ",y)