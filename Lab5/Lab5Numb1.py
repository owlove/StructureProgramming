from array import *
a = array('f',[])
k = 0
for i in range(0,12):
    a.append(float(input("Enter elements: ")))

print("array: ", a)
print("min: ", min(a))
print("min: ", max(a))

for i in range(0,12):
    k = a.index(max(a)) - a.index(min(a))
    if a.index(max(a)) < a.index(min(a)):
        k = a.index(min(a))- a.index(max(a)) - 1

print("kol-vo = ",k)