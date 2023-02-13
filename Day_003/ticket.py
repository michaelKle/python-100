height = int(input("What is you height in cm? "))

if height > 120:
    print("You can ride")
    age = int(input("What is your age? "))
    bill = 0
    if age >= 45 and age <= 55:
        bill = 0
        print("You are in a midlife crises and pay 0$")
    elif age > 18:
        bill = 12
        print("Your ticket is 12$")
    elif age >= 12:
        bill = 7
        print("Your ticket is 7$")
    else:
        bill = 5
        print("Your ticket is 5$")

    want_photos = input("Do you want a photo? (yes/no) ")
    if want_photos == "yes":
        bill += 3
    
    print(f"Your total price is {bill}")


else:
    print("You cant ride, you need to grow ")
