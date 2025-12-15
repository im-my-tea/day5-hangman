import random
import art
import words

print(art.logo)

chosen_word = random.choice(words.word_list)
display = []
for i in chosen_word:
    display += "_"
print(display)
print(" !! " + chosen_word)

end_of_game = False
while not end_of_game:
    guess = input("Guess a letter: ").lower()
    for i in range(len(chosen_word)):
        letter = chosen_word[i]
        if letter == guess:
            display[i] = letter
    print(display)
    if "_" not in display:
        end_of_game = True
        print("You win")