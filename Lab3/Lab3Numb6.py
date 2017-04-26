import math

x = int(input("Enter x: "))
sum = 0
i = 1
s = 1

while s <= x:
    sum = sum + (math.sin(i * x) / i )
    i = i + 2
    s = s + 1
print(sum)