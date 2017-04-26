var = 1
while var < 2 :
   N = int(input("Enter N : "))
   print ("You entered: ", N)
   if (N > 2):
        var = var + 1
   else:
       print("invalid input")
       var = 1

var1 = 1
while var1 < 2 :
   A = float(input("Enter A  : "))
   B = float(input("Enter B  : "))
   if (A < B):
        var1 = var1 + 1
   else:
       print("invalid input, A should be less B")
       var1 = 1

DLN = B - A
H = DLN / N
print("H = ", H)
B1 = A
for i in range(N):
    A1 = B1
    B1 = A1 + H
    print("[",A1,",",B1,"]")