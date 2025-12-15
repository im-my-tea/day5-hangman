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
