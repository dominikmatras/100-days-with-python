import random
import hangman_art
import hangman_words

word_list = hangman_words.word_list
stages = hangman_art.stages

print("Wealcome in Hangman game!\n")

chosen_word = word_list[random.randint(0, len(word_list) - 1)]

placeholder = ""

for letter in chosen_word:
    placeholder += "_"

print(placeholder)

game_over = False
display = ""
correct_letters = []
lives = 6

while not game_over:
    print(f"***************** {lives}/6 LIVES *****************")
    guess = input("Guess the letter: ").lower()

    display = ""

    if guess in correct_letters:
        print("Hey! You already guessed this letter!")

    for letter in chosen_word:
        if letter == guess:
            display += letter
            correct_letters.append(guess)
        elif letter in correct_letters:
            display += letter
        else:
            display += "_"

    if guess not in chosen_word:

        lives -= 1
        if lives == 0:
            game_over = True
            print(stages[lives])
            print(f"\nIt was: {chosen_word.upper()}")
            print("***************** YOU LOSE! *****************")

    if "_" not in display:
        game_over = True
        print(f"\nThe word is: {chosen_word.upper()}")
        print("****************** YOU WIN! *****************")
        lives = 0

    if lives > 0:
        print(stages[lives])
        print("")
        print(display)
