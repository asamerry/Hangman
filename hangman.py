"""
Updates:
 - Added levels
    - Easy
    - Medium
    - Hard
    - Scientific
 - Added specific user input error
 - Now keeps system clear

"""


import random
import string
from pyfiglet import Figlet
import os
import sys


def main():
    os.system("cls")
    previous_guesses = set()
    wrong_guesses = 0
    welcome_player()
    print("Levels: easy(e) / medium(m) / hard(h) / scientific(s)")
    level = pick_level()
    target_word = pick_word(level)
    os.system("cls")
    welcome_player()
    draw_hanged_man(0)
    print("Previous guesses: ")
    print(f"Your word: {build_guessed_word(target_word, previous_guesses)}")
    while True:
        guess = get_player_input(previous_guesses)
        if guess not in target_word:
            wrong_guesses += 1
        previous_guesses.add(guess)
        os.system('cls')
        welcome_player()
        draw_hanged_man(wrong_guesses)
        print(f"Previous guesses: {join_guessed_letters(previous_guesses)}")
        print(f"Your word: {build_guessed_word(target_word, previous_guesses)}")
        if game_over(wrong_guesses, target_word, previous_guesses):
            if wrong_guesses == 6:
                print("\nSorry, you lost!")
            else:
                print("\nCongrats, you won!")
            print(f"Your word was: {target_word}")
            break


def welcome_player():
    figlet = Figlet()
    figlet.setFont(font = "big")
    print(figlet.renderText("Welcome to Hangman!"))


def pick_level():
    while True: 
        try:
            level = input("Select Level: ").strip().lower()
            if level == "e" or level == "easy":
                return 1
            elif level == "m" or level == "medium":
                return 2
            elif level == "h" or level == "hard":
                return 3
            elif level == "s" or level == "scientific" or level == "science":
                return 4
            else:
                print("Not a level.")
                pass
        except KeyboardInterrupt:
            os.system("cls")
            sys.exit()


def pick_word(level):
    if level == 1:
        with open("word_lists/level_easy.txt") as file:
            return random.choice(file.readlines()).strip().lower()
    elif level == 2:
        with open("word_lists/level_medium.txt") as file:
            return random.choice(file.readlines()).strip().lower()
    elif level == 3:
        with open("word_lists/level_hard.txt") as file:
            return random.choice(file.readlines()).strip().lower()
    elif level == 4:
        with open("word_lists/level_scientific.txt") as file:
            return random.choice(file.readlines()).strip().lower()
    else:
        raise ValueError


def get_player_input(previous_guesses):
    while True: 
        try:
            guess = input("Guess a letter: ").lower()
            if len(guess) != 1 or guess not in string.ascii_lowercase:
                print("That's not a letter. Try again.")
            elif guess in previous_guesses:
                print("You already guessed that. Try again.")
            else:
                return guess
        except KeyboardInterrupt:
            os.system("cls")
            sys.exit()


def join_guessed_letters(previous_guesses):
    return " ".join(sorted(previous_guesses))


def build_guessed_word(target_word, previous_guesses):
    built_word = []
    for letter in target_word:
        if letter in previous_guesses:
            built_word.append(letter)
        else:
            built_word.append("_")
    return " ".join(built_word)


def draw_hanged_man(wrong_guesses):
    hanged_man = [
        r"""
      -----
      |   |
          |
          |
          |
          |
          |
          |
          |
          |
    -------
""",
        r"""
      -----
      |   |
      O   |
          |
          |
          |
          |
          |
          |
          |
    -------
""",
        r"""
      -----
      |   |
      O   |
     ---  |
      |   |
      |   |
          |
          |
          |
          |
    -------
""",
        r"""
      -----
      |   |
      O   |
     ---  |
    / |   |
      |   |
          |
          |
          |
          |
    -------
""",
        r"""
      -----
      |   |
      O   |
     ---  |
    / | \ |
      |   |
          |
          |
          |
          |
    -------
""",
        r"""
      -----
      |   |
      O   |
     ---  |
    / | \ |
      |   |
     ---  |
    /     |
    |     |
          |
    -------
""",
        r"""
      -----
      |   |
      X   |
     ---  |
    / | \ |
      |   |
     ---  |
    /   \ |
    |   | |
          |
    -------
""",
    ]

    print(hanged_man[wrong_guesses])


def game_over(wrong_guesses, target_word, previous_guesses):
    return (
        wrong_guesses == 6 or set(target_word) <= previous_guesses
    )


if __name__ == "__main__":
    main()