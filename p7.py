x = float(input("Write x: "))
y = float(input("Write y: "))
i = 1
while (x < y):
    z = x / 10
    x = x + z
    i = i + 1
    z = 0
print("Day: ", i,"Km: ", x)