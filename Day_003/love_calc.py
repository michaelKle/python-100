print("Welcome to the Love Calculator")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")

name_lower = name1.lower() + name2.lower()

count1 = 0
count1 += name_lower.count("t")
count1 += name_lower.count("r")
count1 += name_lower.count("u")
count1 += name_lower.count("e")

count2 = 0
count2 += name_lower.count("l")
count2 += name_lower.count("o")
count2 += name_lower.count("v")
count2 += name_lower.count("e")

score = count1*10 + count2

if score < 10 or score > 90:
    print(f"Your score is {score}, you go together like coke and mentos.")
elif score > 40 and score < 50:
    print(f"Your score is {score}, you are alright together.")
else:
    print(f"Your score is {score}")
