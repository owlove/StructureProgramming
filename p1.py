y = int(input("Write year: "))
if (y % 4 == 0) and (y / 400 == 0) or (y % 100 !=0):
    print("Year Vesokosnui")
else: print("Year not Vesokosnui")