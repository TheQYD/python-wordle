#!python3
import random

def checkWord(guessed_word, chosen_word):
  if guessed_word == chosen_word:
    print('Correct!') 
  
  else:
    print('Sorry! the word was {0}'.format(chosen_word))


def randomizeWord():
  wordbank = ['altar', 'brief', 'cacti', 'dingo']
  return random.choice(wordbank)


if __name__ == '__main__':
  guessed_word = None
  chosen_word = str(randomizeWord())
  print(chosen_word)

  guessed_word = str(input("guess: "))
  checkWord(guessed_word, chosen_word)
