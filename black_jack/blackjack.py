"""
Blackjack main class created by Bruno Trentini
"""
import deck as dk
import player as pl


def insurance():

    option = input(
        "Would you like to take the insurance? [ y / n ]").strip().upper()
    return True


def actions():

    actions = ["Hit", "Stand", "Double Down", "Split", "Surrender"]

    for idx, act in enumerate(actions):
        print(f"\t{idx+1} : {act}")


    while True:
        try:
            action_chosen = int(input("\n\tAction > "))
        except:
            print(f"\t[!] Choose a valid action using numbers 1 to {len(actions)}")
            continue
        else:
            if action_chosen <1 or action_chosen > len(actions):
                print(f"\t[!] Choose a valid action using numbers 1 to {len(actions)}")
                continue
            else:
                break

    return action_chosen


def blackjack():
    '''Starts the game and contains function calls'''

    print(f"\n\tP1     > {player.hand}")
    print(f"\tDealer > {dealer.hand}")

    print("\n\tWhat do you want to do?")
    actions()

    print(player.hand[0][0])



if __name__ == "__main__":

    print("\n=====================================")
    print("\tBLACKJACK")
    print("=====================================")


    # Initialises the Deck
    mydeck = dk.Deck()
    pack = mydeck.shuffle()

    # Initialises player and dealer
    player = pl.Player(player_type="user", balance=500, hand=pack[0:2])
    dealer = pl.Player(player_type="dealer", balance=5000, hand=pack[3:5])

    blackjack()
