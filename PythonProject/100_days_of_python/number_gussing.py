import random

def num_guess(num, guess, attempts):

    if num == guess:
        print(f"you got it! the answer is {num}")
        return True
    elif guess < num:
        print(f"your guess is too low")
        print(f"you have {attempts} attempts left")
        return False
    elif guess > num:
        print(f"your guess is too high")
        print(f"you have {attempts} attempts left")
        return False

def guess_number():
    print("Welcome To The Number Guessing Game!")
    print("I am thinking of a number between 1 and 100.....")
    num = random.randint(1, 100)
    level = input("Choose a difficulty. Type 'easy' or 'hard':")
    if level == "easy":
        print("you have 10 attempts to guess the number.")
        attempts_easy = 10
        for i in range(0,10):
          guess = int(input("make a guess: "))
          attempts_easy -= 1
          guess_check = num_guess(num, guess, attempts_easy)
          if attempts_easy == 0:
              print("\n\nyou've run out of guesses")
          if guess_check or attempts_easy == 0:
              break
    elif level == "hard":
        print("you have 5 attempts to guess the number.")
        attempts_hard = 5
        for i in range(0,5):
            guess = int(input("make a guess: "))
            attempts_hard -= 1
            guess_check = num_guess(num, guess, attempts_hard)
            if attempts_hard == 0:
                print("\n\nyou've run out of guesses")
            if guess_check or attempts_hard == 0:
                break

guess_number()

