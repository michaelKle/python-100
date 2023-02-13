print("Welcome to the tip calculator.")
total = float(input("What was the total bill? $"))
percentage = int(input("What percentage tip would you like to give? 10, 12, or 15? "))
num_people = int(input("How many people to split the bill? "))

#total = 124.56
#percentage = 12
#num_people = 7

tip = (total / num_people) * (1+ percentage/100)

amount = round(tip, 2)
amount_format = "{:.2f}".format(amount)
print(f"Each person should pay: ${amount_format}")

