import math

x = int(input("Enter x: "))
sum = 0
i = 0 # счетчик
s = 1 # увеличение значения

while i <= x:
    sum = sum + (math.sin(s * x) / s )
    s += 2
    i += 1
print(sum)