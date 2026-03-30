import game_data, random

logo = r"""
    __  ___       __             
   / / / (_)___ _/ /_  ___  _____
  / /_/ / / __ `/ __ \/ _ \/ ___/
 / __  / / /_/ / / / /  __/ /    
/_/ ///_/\__, /_/ /_/\___/_/     
   / /  /____/_      _____  _____
  / /   / __ \ | /| / / _ \/ ___/
 / /___/ /_/ / |/ |/ /  __/ /    
/_____/\____/|__/|__/\___/_/     
"""

vs = r"""
 _    __    
| |  / /____
| | / / ___/
| |/ (__  ) 
|___/____(_)
"""

def compare_answer(A,B, guess):
    if (A > B and guess == "A") or (B > A and guess == "B"):
        return True
    else:
        return False

def game(logo,vs):
    print(logo)
    dataset = game_data.data

    is_game_over = False
    score = 0
    while not is_game_over:
        random_accs = random.sample(dataset, 2)
        opp1 = random_accs[0]
        opp2 = random_accs[1]

        print(f"Compare A: {opp1["name"]}, a {opp1["description"]} from {opp1['country']}")
        print("\n"+vs+"\n")
        print(f"compare B: {opp2["name"]}, a {opp2["description"]} from {opp2['country']}")
        guess = input("who has more followers on instagram? A or B:")
        answer = compare_answer(opp1["follower_count"], opp2["follower_count"], guess)
        if answer:
            score += 1
            print("you are correct! lets move on to the next!\n\n")
            print("\033c", end="")

        else:
            print(f"you loose! your final score is {score}")
            is_game_over = True
game(logo,vs)








