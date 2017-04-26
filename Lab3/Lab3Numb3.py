p = int(input("write p: "))
q = int(input("write q: "))

p1 = []
q1 = []
qp = []

for i in range(1,q + 1):
    if (q % i == 0) and (q / 1 == q):
        q1.append(i)
print(q1)

for j in range(1,p + 1):
    if (p % j == 0) and (p / 1 == p):
        p1.append(j)
print(p1)

for i in q1:
    if i in p1:
        qp.append(i)
print(qp)