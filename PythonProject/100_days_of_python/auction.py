

def bid_win(bids):
    winner = max(bids, key=bids.get)
    print(f"the winner of the auction with a maximum bid of {bids[winner]} is {winner}")

con = True
bids = {}
while con:
    name = input("What is your name? ")
    bid = int(input("What is your bid? "))
    bids[name] = bid
    looping = input("Is there anyone other than you to bid? yes or no: ")
    if looping == "yes":
        print("\033c", end="")
    else:
        print("\033c", end="")
        con = False
        bid_win(bids)
