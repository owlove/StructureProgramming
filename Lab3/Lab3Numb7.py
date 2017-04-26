import math

i = 0.1

while i <= 2.7:
    y = math.fabs(i**2 - 4) + 0.25 * i - 2
    i = i + 0.1
print(y)