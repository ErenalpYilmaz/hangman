import random
from hangman_words import word_list

from hangman_art import stages
from hangman_art import logo
print(logo)
chosen_word = random.choice(word_list)
print(chosen_word)

# TODO: Create a "placeholder" with the same number of blanks as the chosen_word
placeholder = ''
word_leght = len(chosen_word)
for i in range(1,word_leght):
    placeholder+="_"
print(placeholder)

correct_letters = []

game_over = False
lives = 6
while not game_over:
    
    display = ""
    guess = input("Guess a letter : ")
    if guess in correct_letters:
        print("You've already guessed this letter")
    for letter in chosen_word:
        if guess == letter:
            display+= guess
            correct_letters.append(guess)
        elif letter in correct_letters:
            display += letter
        else:
            display += "_"

    if guess not in chosen_word:
            print(f"Your letter is not in the word.\nYour letter = {guess}")
            lives -= 1
            if lives == 0:
                game_over = True
                print(f"IT WAS CORRECT WORD = {chosen_word}  YOU LOSE !!!!")
            
    print(stages[lives])
    
    if display == chosen_word:
        print("You Win !")
        game_over = True
    
    print(display)
