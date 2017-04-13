import math
y = float(input("Write number (y): "))
r = float(input("Write number (r): "))
t = float(input("Write number (t): "))

w = (4 * math.pow(t,3) + math.log1p(r))/(math.pow(math.e,y + r) + 7.2 * math.sin(r))
print(w)