#!python3
import random

guesses = 0
guessed_word = None
chosen_word = None

def checkWord(guessed_word, chosen_word):
  if guessed_word == chosen_word:
    print('Correct!') 
  
  else:
    print(guesses)
    if guesses < 5:
      print('Try again.')
    else:
      print('Better luck next time.')


def randomizeWord():
  wordbank = ['altar', 'brief', 'cacti', 'dingo']
  return random.choice(wordbank)


if __name__ == '__main__':
  chosen_word = str(randomizeWord())
  print(chosen_word)

  while guesses < 5:
    guessed_word = str(input("Enter your guess (tries left: {0}): ".format(5-guesses)))
    guesses += 1
    checkWord(guessed_word, chosen_word)
