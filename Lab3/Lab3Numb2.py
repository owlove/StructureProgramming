import math

k = int(input("write k: "))
n = -3
z = 1

for i in range(n,k):
    z = z * (((n + 2) * math.fabs(n - 4)) / math.factorial(n + 3))
print("sum = ", z)