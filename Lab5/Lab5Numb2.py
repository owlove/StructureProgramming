from array import *
a = array('i',[])
sm = 0
ort = 0

for i in range(0,10):
    a.append(int(input("Enter elements: ")))
print("array: ", a)

for i in range(0,10):
    if a[i] < 0:
        otr = i
        break     # пока так

for i in range(0,otr):
    sm += a[i]

print("kol-vo = ", otr)
print("sum = ", sm)
