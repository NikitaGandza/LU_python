import random
import re


class Game:
    def __init__(self):
        self.words_to_guess = ["apple", "smartphone", "lemon", "flower"]
        self.word_to_guess = ""
        self.words_to_guess_hidden = ""
        self.guess_count = 0
        self.hangman_full_clean = " +---+\n |   |\n     |\n     |\n     |\n     |\n========="
        self.hangman_full = " +---+\n |   |\n     |\n     |\n     |\n     |\n========="
        self.index_to_change = [
            [15, "*"],
            [21, "/"],
            [22, "|"],
            [23, '\\'],
            [28, "/"],
            [30, '\\']
        ]

    def change_char(self, index):
        self.hangman_full = self.hangman_full[:index[0]] + index[1] + self.hangman_full[index[0] + 1:]

    def append_new_word(self, word):
        self.words_to_guess.append(word)


def main():
    game = Game()

    while True:
        game_setting = int(input("Enter 1 to play hangman, 2 to add a new word, 3 to quit program\n\nEnter number: "))
        if game_setting == 3:
            break
        elif game_setting == 2:
            new_word = input("\nEnter new word: ")
            game.append_new_word(new_word)
            print(f"{new_word} applied")
        elif game_setting == 1:
            game.hangman_full = game.hangman_full_clean
            word_to_guess = random.choice(game.words_to_guess)
            game.words_to_guess_hidden = len(word_to_guess)*"-"
            print(game.hangman_full)
            wrong_guess_counter = 0
            guessed_letters = ''
            while wrong_guess_counter < 6 and "-" in game.words_to_guess_hidden:
                print(f"Guessed letters:{guessed_letters}\n{game.words_to_guess_hidden}")
                new_letter = input("Enter letter: ")
                guessed_letters += " "+new_letter
                if new_letter in word_to_guess:
                    print(new_letter)
                    indexes = [i.start() for i in re.finditer(new_letter, word_to_guess)]
                    for i in indexes:
                        game.words_to_guess_hidden = game.words_to_guess_hidden[:i] + new_letter + game.words_to_guess_hidden[i + 1:]
                    print(game.hangman_full)
                else:
                    game.change_char(game.index_to_change[wrong_guess_counter])
                    wrong_guess_counter += 1
                    print(wrong_guess_counter)
                    print(game.hangman_full)

            if wrong_guess_counter >= 6:
                print("You lose!")
            else:
                print("You win!")


if __name__ == '__main__':
    main()
