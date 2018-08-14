# Python tic tac tow
from IPython.display import clear_output

P1_PREF = 0

def choose_option():

    while True:
        P1_PREF = input("First, let's get player's 1 preference: X or O? \n").upper()

        if P1_PREF not in ['X','O']:
            continue
        else:
            break

    print(f"Player one has chosen {P1_PREF}")

    return P1_PREF

def print_board(option):

    if option == "ok":
        return False
    
    board = [range(1,9)]
    print(board)

    return True

def main():

    GAME = True

    print("Welcome to the tic-tac-toe game")
    choose_option()

    p = 1

    while GAME:

        option = input(f"P{p}: ").upper()
        GAME = print_board(option)

        if p == 2:
            p == 1

main()
