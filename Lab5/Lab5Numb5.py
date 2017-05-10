import random
n = 5

a = [[random.randint(-9,9) for j in range(0,5)] for i in range(0,5)]

for i in range(0,5):
    for j in range(0,5):
        print(a[i][j], end = ' ')
    print()

for i in range(0,1):
    for j in range(0,n):
        if a[i][j] < 0:
            a[i][j] = 0

print("------------")

for i in range(0,5):
    for j in range(0,5):
        print(a[i][j], end = ' ')
    print()