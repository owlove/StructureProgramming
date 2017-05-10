a = int(input("Enter number: "))
p =[]
ai = 0 #max index
bi = 0 #min index

p.append(int(str(input("Enter element: ")), 2))
a1 = p[0]
b = p[0]

for i in range(1,a):
    p.append(int(str(input("Enter element: ")),2))
    if p[i] > a1:
        ai = i
        a1 = p[i]
    if p[i] < b:
        bi = i
        b = p[i]

print(p)

p[ai], p[bi] = p[bi], p[ai]

for j in p:
    print(bin(j), end = ', ')
