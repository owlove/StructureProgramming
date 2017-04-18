s = int(input("write number (4): "))
f = []
a = 1000

while a > 0:
    f.append((s // a) % 10)
    a = a // 10
print(f)

if(f[0] + f[1] == f[2] + f[3]):
    print("ravna")
else: print("ne ravna")

if (sum(f) % 7 == 0):
    print("kratno 7")
else: print("ne kranto 7")

