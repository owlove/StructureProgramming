S = str(input("Enter string: "))
M =[]
F =[]
for i in range(0,len(S)):
    M.append(ord(S[i]))
    if M[i] == 1103:
        M[i] = 32
    else:
        M[i] = M[i] + 1

for i in range(0,len(S)):
    F.append(chr(M[i]))

print(' '.join(F))
