import random
n = int(input("Enter number n: "))
pr = 1

a = [[random.randint(1,9) for j in range(0,n)] for i in range(0,n)]

for i in range(0,n):
    for j in range(0,n):
        print(a[i][j], end = ' ')
    print()

for i in range(0,1):
    for j in range(0,n):
        pr *= a[i][j]

print("Proizvedenie the first line = ", pr)