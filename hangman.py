import random
from words import words
import string

def getValidWord(words):
    word = random.choice(words)
    while '-' in word or ' ' in word:
        word = random.choice(words)
    return word

def hangman():
    word = getValidWord
    wordLetters = set(word)
    alphabet = set(string.ascii_uppercase)
    usedLetters = set()
    lives = 6
    while len(wordLetters) > 0 and lives > 0:

        print('You have used these letters:', ''.join(usedLetters))
        wordList = [letter if letter in usedLetters else '-' for letter in word]
        print('Current Word: ', ' '.join(wordList))

     userLetter = input('Guess a letter: ').upper()
     
        if userLetter in alphabet - usedLetters:
        usedLetters.add(userLetter)
        if userLetter in wordLetters:
            wordLetters.remove(userLetter)

            else: lives = lives - 1 
                print('Letter is not in word.')
        elif userLetter in usedLetters:
            print("You've already used that letter, please try again.")
        else:
        print('Invalid Character, please try again.')

        if lives == 0:
            print('You died, sorry. The word was', word)
        else
            print('You guessed the word', word, '!!')