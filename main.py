import random
import art
import words

print(art.logo)

chosen_word = random.choice(words.word_list)
display = []
for i in chosen_word:
    display += "_"
print(display)

end_of_game = False
lives = 6
while not end_of_game:
    guess = input("Guess a letter: ").lower()
    for i in range(len(chosen_word)):
        letter = chosen_word[i]
        if letter == guess:
            display[i] = letter
    if guess not in chosen_word:
        lives -= 1
        print(f"Your guess {guess} is not in the word. You lose a life. Lives left: {lives}")
    if lives == 0:
        end_of_game = True
        print("You lose")
        break
    print(display)
    if "_" not in display:
        end_of_game = True
        print("You win")
        break
    print(art.stages[lives])