import random

print("Welcome to the PyPassword Generator!")
#num_characters = int(input("How many characters would you like your password to be long?\n"))
#num_symbols = int(input("How many symbols would you like?\n"))
#num_numbers = int(input("How many numbers would you like?\n"))

num_characters = 12
num_symbols = 3
num_numbers = 3
num_letters = num_characters - num_numbers - num_symbols

symbols = ['!', '#', '§', '%', '&', '?']
numbers = [chr(item + ord('0')) for item in range(0, 10)]
letters = [chr(item + ord('a')) for item in range(0, 26)] + [chr(item + ord('A')) for item in range(0, 26)]


password = []
for n in range(0, num_symbols):
    password.append(random.choice(symbols))

for n in range(0, num_numbers):
    password.append(random.choice(numbers))

for n in range(0, num_letters):
    password.append(random.choice(letters))

random.shuffle(password)
print(f"Your final password is {''.join(password)}")