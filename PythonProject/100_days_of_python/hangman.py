import random
from operator import indexOf

words = ["aadvark","baboon","camel"]
chosen_word = random.choice(words)
spaces = list('_'*len(chosen_word))
end_of_game = False
print(str(spaces))

hangman_stages = [
    r"""
   +---+
   |   |
       |
       |
       |
       |
=========
""",
    r"""
   +---+
   |   |
   O   |
       |
       |
       |
=========
""",
    r"""
   +---+
   |   |
   O   |
   |   |
       |
       |
=========
""",
    r"""
   +---+
   |   |
   O   |
  /|   |
       |
       |
=========
""",
    r"""
   +---+
   |   |
   O   |
  /|\  |
       |
       |
=========
""",
    r"""
   +---+
   |   |
   O   |
  /|\  |
  /    |
       |
=========
""",
    r"""
   +---+
   |   |
   O   |
  /|\  |
  / \  |
       |
=========
"""
]
lives = 0

while not end_of_game:

    guess = input("Guess a letter: ").lower()
    display = ""
    if guess in chosen_word:

        for i in range(len(chosen_word)):
            if chosen_word[i] == guess:
                display += chosen_word[i]
            else:
                display += "_"
        print(display)
    else:
        print(f"wrong guess"
              f"{hangman_stages[lives]}")

        lives += 1
        if lives == 6:
            end_of_game = True
            print("you lose")
    if "_" not in spaces:
        end_of_game = True
        print("you win")



