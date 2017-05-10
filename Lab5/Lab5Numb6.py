import random
n = int(input("Enter number n: "))
t = 1
a = [[random.randint(1,9) for j in range(0,n)] for i in range(0,n)]

for i in range(0,n):
    for j in range(0,n):
        print(a[i][j], end = ' ')
    print()

for i in range(0,n):
        for j in range(0,n):
            if a[i][j] != a[j][i]:
                t = 0
                break
        if (t == 1 ):
            break
if (t == 1):
   print("true")
else: print("false")
