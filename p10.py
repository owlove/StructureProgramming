sp = ["0","1","2","3","4","5","6","7","8","9"]
c = input("Write symbol: ")
c = str(c)
a = False
for i in range(0, 10):
    if sp[i] == c:
        a = True
        break
    else:
        s = False
if a == True:
    print("yes")
else: print("no")