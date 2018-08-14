'''
Python tictactoe game as exercise for udemy's training
'''
from random import randint

players = ["", ""]
board = [f" {i+1} " for i in range(0, 9)]
player = 0
game_on = True
again = "Y"


def validate_entry(position):

    global board
    print(type(position), " : ", position)

    if position in [x for x in range(1, 10)] \
            and position in \
                [int(x.strip()) if x.isdigit() else -99 for x in list(set(board))]:
        return True


def check_outcome():

    global game_on
    global player

    if len(set(board[6:9])) == 1:
        game_on = False
    elif len(set(board[3:6])) == 1:
        game_on = False
    elif len(set(board[0:3])) == 1:
        game_on = False
    elif len(set(board[::4])) == 1:
        game_on = False
    elif len(set(board[2:8:2])) == 1:
        game_on = False
    elif len(set(board[::])) == 2:
        player = "NINGUEM "
        game_on = False
    else:
        return game_on


def update_board(position):

    global board

    board[position] = f" {players[player - 1]} "


def print_board():

    print("")
    print(" | ".join(board[6:9]))
    print(" | ".join(board[3:6]))
    print(" | ".join(board[0:3]))


def move():

    global player

    if player == 0:
        player = randint(1, 2)
    if player == 1:
        player = 2
    else:
        player = 1

    item = players[player - 1]
    msg = f"\n [ P{player} ] > where do you want to place your {item}?: "
    position = int(input(f"{msg}").strip())

    if validate_entry(position):
        position = position - 1
        print("OK")
    else:
        print("INVALID")

    return position


def define_players():

    global players

    options = ["X", "O"]

    while players[0] not in options:
        players[0] = input(
            f"P1 do you want {options[0]} or {options[1]}?: ").upper().strip()

    players[1] = options.pop(options not in players)

    return players


def reload():

    global players
    global board
    global player
    global game_on
    global again

    players = ["", ""]
    board = [f" {i+1} " for i in range(0, 9)]
    player = 0
    game_on = True
    again = "Y"


def main():

    global again

    print("==== \tTIC TAC TOE v1\t ====")

    while again == "Y":
        reload()
        define_players()

        while game_on:
            print_board()
            update_board(move())
            check_outcome()

        print(f"\n\t {player} GANHOU!\n")
        print_board()
        print("\n\t -- end\n")

        again = input("Play again? [ y / any key to exit ]: ").upper().strip()


main()
