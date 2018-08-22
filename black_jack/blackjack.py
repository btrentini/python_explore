"""
Blackjack main class created by Bruno Trentini
"""
import deck as dk
import player as pl
import hand as hd


def check_play():
    '''Checks game progress and actions taken'''
    pass


def actions():
    '''Allow user to choose an action. Eg: Hit or Surrender'''

    actions = ["Hit", "Stand", "Double Down", "Split", "Surrender"]

    print("\n\tWhat do you want to do?")

    for idx, act in enumerate(actions):
        print(f"\t{idx+1} : {act}")

    while True:
        try:
            action_chosen = int(input("\n\tAction > "))
        except ValueError:
            print(
                f"\t[!] Choose a valid action using numbers 1 to {len(actions)}")
            continue
        else:
            if action_chosen < 1 or action_chosen > len(actions):
                print(
                    f"\t[!] Choose a valid action using numbers 1 to {len(actions)}")
                continue
            else:
                break

    return action_chosen


def bet():
    '''Gets an input regarding the player's bet'''

    print(
        f"\n\tP1  > How much you want to bet? \t | Your balance: {PLAYER.balance}")

    while True:
        try:
            bet = int(input("\n\tBet > "))
        except ValueError:
            print(
                f"\t[!] Choose a valid action using whole numbers")
            continue
        else:
            if bet < 1 or bet > PLAYER.balance:
                print(
                    f"\t[!] Enter a valid number. Your balance is {PLAYER.balance}")
                continue
            else:
                break

    PLAYER.update_balance(-bet)

    print(f"\n\tP1     > {PLAYER.print_hand()}")
    print(f"\tDealer > {PLAYER.print_hand()}")


def blackjack():
    '''Starts the game and contains function calls'''
    bet()
    check_play()
    actions()


if __name__ == "__main__":

    print("\n=====================================")
    print("\tBLACKJACK")
    print("=====================================")

    # Initialises the Deck
    MYDECK = dk.Deck()
    PACK = MYDECK.shuffle()

    # Initialises player and dealer
    PLAYER = pl.Player(player_type="user", balance=500,
                       hand=hd.Hand(PACK[0:2]))
    DEALER = pl.Player(player_type="dealer", balance=5000,
                       hand=hd.Hand(PACK[3:5]))

    blackjack()
