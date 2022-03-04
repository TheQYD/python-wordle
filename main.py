#!python3

import random

guesses = 0
max_guesses = 6

#TODO: Fix "guesses referenced before assignment" bug.

def checkWord(guessed_word, chosen_word):
  if guessed_word == chosen_word:
    print('Correct!')
  
  else:
    if guesses < max_guesses-1:
      print('Try again.')
    else:
      print('Better luck next time.')

def randomizeWord():
  wordbank = ['altar', 'brief', 'cacti', 'dingo']
  return random.choice(wordbank)

def startGame(): 
  while guesses < max_guesses:
    guessed_word = str(input("Enter your guess (tries left: {0}): ".format(max_guesses-guesses)))
    guesses += 1
    checkWord(guessed_word, chosen_word)

if __name__ == '__main__':
  chosen_word = str(randomizeWord())
  startGame()

  print(chosen_word)
  

