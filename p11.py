st = input("Write String: ")
wd = 0
st = st + " "
for i in range(0, len(st)):
    if (st[i] == " ") and (st[i-1] != " "):
        wd = wd + 1
print("Words: ", wd)