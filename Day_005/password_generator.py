import random

print("Welcome to the PyPassword Generator!")
num_characters = int(input("How many characters would you like your password to be long?\n"))
num_symbols = int(input("How many symbols would you like?\n"))
num_numbers = int(input("How many numbers would you like?\n"))

#num_characters = 12
#num_symbols = 3
#num_numbers = 3
num_letters = num_characters - num_numbers - num_symbols

symbol_chance = num_symbols / num_characters
number_chance = num_numbers / num_characters
letter_chance = num_letters / num_characters

symbols = ['!', '#', '§', '%', '&', '?']
numbers = [chr(item + ord('0')) for item in range(0, 10)]
letters = [chr(item + ord('a')) for item in range(0, 26)] + [chr(item + ord('A')) for item in range(0, 26)]

password = ''
while True:
    if num_symbols > 0 and random.random() < symbol_chance:
        symbol = random.choice(symbols)
        print(f"Picked symbol '{symbol}'")
        password += symbol
        num_symbols -= 1

    if num_numbers > 0 and random.random() < number_chance:
        number = random.choice(numbers)
        print(f"Picked number '{number}'")
        password += number
        num_numbers -= 1

    if num_letters > 0 and random.random() < letter_chance:
        letter = random.choice(letters)
        print(f"Picked letter '{letter}'")
        password += letter
        num_letters -= 1

    if len(password) == num_characters:
        break

print(f"Your final password is {password}")