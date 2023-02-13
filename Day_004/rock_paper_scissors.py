import random

scissors = r'''
   _       ,/'
  (_).  ,/'
   _  ::
  (_)'  `\.
           `\.
'''

paper = r'''
       .-.________
  ----/ \ )_______)
     (  (/()___)
          ()__)
  ----\___()_)
'''

rock = '''
       ,--.--._
------" _, \___)
        / _/____)
        \//(____)
------\     (__)
       `-----"
'''

game_images = [rock, paper, scissors]
choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper, or 2 or Scissors\n"))
if choice < 0 or choice > 2:
    print("Invalid input - you loose")
    exit()

print(game_images[choice])


print("Computer choose:")
computer_choice = random.randint(0, 2)
print(game_images[computer_choice])

loose = "You loose"
draw = "It's a draw"
win = "You win"
results = [[draw, loose, win],[win, draw, loose],[loose, win, draw]]

print(results[choice][computer_choice])