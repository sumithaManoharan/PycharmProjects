# city = input("what is the name of the city you grew up in?")
# pet = input("what is the name of the pet you grew up in?")
#
# print(f"the name of your band is {city} {pet}")
import random

# print("Welcome to the tip calculator!")
# bill = float(input("enter the bill amount"))
# percent = int(input("enter the percent of bill? 10, 12 or 15"))
# per = int(input("How many people should split the bill?"))
# tip = bill/per + (bill * percent/100)/per
#
# print(f"the tip each person should give is {round(tip, 2)} ")

# 'r' is used for Raw String to handle backslashes safely

# game_images = [
#     # Rock (Index 0)
#     r"""
#     _______
# ---'   ____)
#       (_____)
#       (_____)
#       (____)
# ---.__(___)
#     """,
#
#     # Paper (Index 1)
#     r"""
#     _______
# ---'   ____)____
#           ______)
#           _______)
#          _______)
# ---.__________)
#     """,
#
#     # Scissors (Index 2)
#     r"""
#     _______
# ---'   ____)____
#           ______)
#        __________)
#       (____)
# ---.__(___)
#     """
# ]
# game_choice = random.randint(0, len(game_images) - 1)
# user_choice = int(input("Enter your choice: 0 for rock, 1 for paper, 2 for scissors: "))
# print(game_images[game_choice])
# if user_choice == 0 and game_choice > 0:
#     print("you win!")
# elif user_choice == 1 and game_choice == 0:
#     print("you win!")
# elif user_choice == 1 and game_choice == 2:
#     print("you loose!")
# elif user_choice == 2 and game_choice == 0:
#     print("you loose!")
# elif user_choice == 2 and game_choice == 1:
#     print("you win!")
# elif user_choice == game_choice:
#     print("its a draw! try again!")


import random
let_dict={
'letters' : ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'],
'numbers' : ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9'],
'symbols' : ['!', '#', '$', '%', '&', '(', ')', '*', '+'] }

print("Welcome to the PyPassword Generator!")
nr_letters = int(input("How many letters would you like in your password?\n"))
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

for key, value in let_dict.items():
    password = [random.choice(key) for key in range(1,{value}+1)]
    print(password)

