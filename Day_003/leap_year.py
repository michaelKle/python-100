year = int(input("Which year do you want to check? "))

evenly_by_4 = year % 4 == 0
evenly_by_100 = year % 100 == 0
evenly_by_400 = year % 400 == 0

if evenly_by_400:
    print(f"{year} is a leap year - divisble by 400")
elif evenly_by_100:
    print(f"{year} is not a leap year - divisble by 100 but not 400")
elif evenly_by_4:
    print(f"{year} is a leap year - not divisble by 100 but by 4")
else:
    print(f"{year} is not a leap year - not divisible by 4")
    
