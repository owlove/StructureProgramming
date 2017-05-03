S = str(input("Enter string: "))

first = int
last = int

for i in range(0,len(S)):
    if "привет" in S:
        first = S.find("привет")
        last = first + 7
        S1 = S[0:first]
        S2 = S[last:len(S)]
        S = S1 + S2
print(S)