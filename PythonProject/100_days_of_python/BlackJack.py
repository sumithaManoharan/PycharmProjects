import random

def sum_cards(s_cards):
    if 11 in s_cards and sum(s_cards) > 21:
        s_cards.remove(11)
        s_cards.append(1)
        return sum(s_cards)
    else:
        return sum(s_cards)


def blackjack():

    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    user = random.sample(cards, 2)
    dealer = random.sample(cards, 2)
    is_game_over = False

    while not is_game_over:
        sum_user = sum_cards(user)
        sum_dealer = sum_cards(dealer)
        print(f"your cards: {user},your current score: {sum_user}")
        print(f"dealer first card: {dealer[0]}")
        if sum_user > 21 or sum_dealer > 21:
            is_game_over = True
        else:
            hit = input("would you like to go for a hit? yes or no:")
            if hit == "yes":
                user.append(random.choice(list(cards)))
            else:
                is_game_over = True

    while sum_dealer < 21 and sum_dealer < 17:
        dealer.append(random.choice(list(cards)))
        sum_dealer = sum_cards(dealer)

    print(f"   Your final hand: {user}, final score: {sum_user}")
    print(f"   Dealer's final hand: {dealer}, final score: {sum_dealer}")

    if sum_user > 21:
        print("You went over. You lose! 😭")
    elif sum_dealer > 21:
        print("Dealer went over. You win! 😁")
    elif sum_user == sum_dealer:
        print("It's a draw! 🤝")
    elif sum_user == 0:
        print("Win with a Blackjack! 😎")
    elif sum_dealer == 0:
        print("Lose, opponent has Blackjack! 😱")
    elif sum_user > sum_dealer:
        print("You win! 😃")
    else:
        print("You lose! 😤")


blackjack()