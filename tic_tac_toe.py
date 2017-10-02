###############
# TIC TAC TOE #
###############

import os

player_one = '[X]'
player_two = '[O]'
_size_of_board = int(input("How large do you want the board to be?\n> "))
board = [[None] * _size_of_board for i in range(_size_of_board)]
moves = []
popped = []


class Move:
    def __init__(self, row, col, player):
        self.row = row
        self.col = col
        self.player = player


def move(row, col, player):
    if player == player_one:
        board[row - 1][col - 1] = player_one
    else:
        board[row - 1][col - 1] = player_two
    moves.append(Move(row, col, player))
    draw_board()
    print("moves {}, row: {}, col: {}, player: {}".format(
        moves, moves[0].row, moves[0].col, moves[0].player))


def draw_board():
    os.system('clear')
    for row in board:
        for col in row:
            if col is None:
                print('[ ]', end='')
            else:
                print(col, end='')
        print('')


def undo():
    undo_move = moves.pop()
    popped.append(undo_move)
    board[undo_move.row - 1][undo_move.col - 1] = None
    draw_board()
    print("removed {} from the 'moves' list".format(popped))


def redo():
    redo_move = popped.pop()
    moves.append(redo_move)
    board[redo_move.row - 1][redo_move.col - 1] = redo_move.player
    draw_board()
