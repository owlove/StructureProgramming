import math

var = 1
while var < 2 :
   N = float(input("Enter N : "))
   if (N >= 1) and (N <= 1000):
        var = var + 1
   else:
       print("invalid input")
       var = 1

M = float(input("Enter M: "))
Res = math.pow((N // M), 2)

print(Res)
