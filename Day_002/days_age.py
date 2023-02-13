print("Welcome to the days age calculator.")
age = input("What is your current age?")

# 1 year = 365 days
# 1 year = 52 weeks
# 1 year = 12 month
# till 90

years_left = 90 - int(age)
month_left = years_left * 12
weeks_left = years_left * 52
days_left = years_left * 365

print(f"You have {days_left} days, {weeks_left} weeks, and {month_left} months left.")