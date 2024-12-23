# wordle.py

import pathlib
import random
from string import ascii_letters
from rich.console import Console
from rich.theme import Theme

console = Console(width=40,
                  theme=Theme({"correct" : "bold white on green",
                               "misplaced" : "bold white on red",
                               "incorrect":"bold white on #666666"
                              }))

def refresh_page(headline, guesses):
    """Refresh the page for each guess"""
    console.clear()
    console.rule(f":leafy_green: {headline} :leafy_green:")

    for guess in guesses:
        console.print(f"{guess}", justify="center")


def get_secret_word(file_name):
    """Get a random secret word from the words list"""
    # Get the list of words from the words text file
    words = [word.lower() for word in pathlib.Path(file_name).read_text().split("\n")]

    # Choose a random word for this round from words list
    return random.choice(words)


def show_guess(secret_word, guess):
    """Show the user's guess in the terminal and classify all letters"""
    # Check for the letters that are correctly guessed and placed correctly
    styled_guesses = []
    for guess in guess:
        styled_string = []
        for letter, correct in zip(guess, secret_word):
            if letter == correct:
                style = "bold white on green"
            elif letter in secret_word:
                style = "bold white on yellow"
            elif letter in ascii_letters:
                style = "bold white on #666666"
            else:
                style = "dim"
            styled_string.append(f"[{style}]{letter}")
        styled_guesses.append("".join(styled_string))
    refresh_page(f"Wordle", styled_guesses)


def game_over(answer):
    """End the game as the turns exhausted"""
    print("Oh oh, You have exhausted your chances.")
    print(f"The secret word was {answer}")


def main():
    # Pre-Process
    secret_word = get_secret_word('words.txt')
    guesses = ["_" * 5] * 6
    refresh_page(f"Wordle", guesses)
    # Process
    for turn in range(6):


        guesses[turn] = input("Guess a word: ").lower()

        show_guess(secret_word, guesses)

        if secret_word == guesses[turn]:
            refresh_page(f"Wordle - Guess No {turn + 1}", guesses)
            print("Yay, you guessed the word correctly")
            break

    # Post-Process
    else:
        refresh_page(f"Wordle - Game Over", guesses)
        game_over(secret_word)


if __name__ == "__main__":
    main()