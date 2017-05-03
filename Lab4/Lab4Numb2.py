S = str(input("Enter string: "))
M =[]
F =[]
for i in range(0,len(S)):
    M.append(ord(S[i]))
    M.sort()

for i in range(0,len(S)):
    F.append(chr(M[i]))

print(' '.join(F))