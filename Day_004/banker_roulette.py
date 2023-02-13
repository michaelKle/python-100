import random

name_string = input("Give me everybody's names, separated by a comma. \n")
names = name_string.split(",")

no = random.randint(0, len(names)-1)
print(f"Fortuna picked {names[no]}")
print(f"On second try {random.choice(names)}")
