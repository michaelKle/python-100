height = float(input("enter you height in m: "))
weight = float(input("enter you weight in kg: "))

bmi = weight / height**2

print(f"You BMI is {bmi}")

if bmi < 18.5:
    print("You are underweight")
elif bmi < 25:
    print("You are normal weight")
elif bmi < 30:
    print("You are overweight")
elif bmi < 35:
    print("Your are obese")
else:
    print("You are clinically obese")
