import math

x = int(input("Enter x: "))
sum = 0
s = 1 # увеличение значения

for i in range(0,x):
    sum1 = (math.sin(s * x)/ s)
    sum += sum1
    s += 2
print(sum)