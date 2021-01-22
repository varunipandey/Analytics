import random
from words import words
import string

def get_valid_word(words):
    word = random.choice(words)
    while '-' in word or ' ' in word:
        word = random.choice(words)
    return word.upper()

def hangman():
    word = get_valid_word(words)
    word_letters = set(word) #letters in the word
    alphabet = set(string.ascii_uppercase)
    used_letters = set() #what the user has guessed

    lives = 7

    #getting user input
    while len(word_letters) > 0 and lives > 0:
        print("You have ", lives, "lives left. \n You have used these letters", " ".join(used_letters))
        word_list = [letter if letter in used_letters else "-" for letter in word]
        print("Current word:", ' '.join(word_list))
        user_letter = input("Guess a letter: ").upper()
        if user_letter in alphabet - used_letters:
            used_letters.add(user_letter)
            if user_letter in word_letters:
                word_letters.remove(user_letter)
            else:
                lives = lives - 1
                print("Letter is not in the word")

        elif user_letter in used_letters:
            print("You have already guessed that character")
        else:
            print("Invalid character. Please try again")

    if lives == 0:
       print("You have died, Sorry! The word was ", word)
    print("You guessed ", word, " correctly!")



hangman()

