import math
a = float(input("введите сторону а: "))
b = float(input("введите сторону b: "))
c = float(input("введите сторону c: "))

if (a < (b + c)) and (b < (a + c)) and (c < (a + b)):
    ma = round(0.5 * math.sqrt(2 * (b**2) + 2 * (c**2) - (a**2)),3),
    mb = round(0.5 * math.sqrt(2 * (a**2) + 2 * (c**2) - (b**2)),3),
    mc = round(0.5 * math.sqrt(2 * (b**2) + 2 * (a**2) - (c**2)),3),
    print( "медиана к стороне а = ", ma, "\nмедиана к стороне b = ", mb, "\nмедиана к стороне с = ", mc)
else: print("Введенные стороные не образуют треугольник!")