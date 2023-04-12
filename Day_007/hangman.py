import random

# https://gist.github.com/chrishorton/8510732aa9a80a03c829b09f12e20d9c
HANGMANPICS = ['''
  +---+
  |   |
      |
      |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========''']


def printHangman(hangman):
    print(HANGMANPICS[hangman])


words = ["ardvark", "baboon", "camel"]
chosenWord = random.choice(words)
wordWithUnderscores = list("_" * len(chosenWord))
hangman = 0

while True:
    print(f"Your current progress: {str(wordWithUnderscores)}")
    nextletter = input("Guess next letter ")
    positions = [i for i in range(len(chosenWord)) if chosenWord.startswith(nextletter, i)]
    for idx in positions:
        wordWithUnderscores[idx] = nextletter

    if len(positions) == 0:
        print("Not part of the word!")
        hangman += 1
        printHangman(hangman)

    if wordWithUnderscores.count("_") == 0:
        print(f"You win!! The word is {str(wordWithUnderscores)}")
        break

    if hangman == 6:
        print("You loose!")
        break
