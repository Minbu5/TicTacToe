from board import Tboard
from player import Player

board = Tboard()
pl_1 = Player('X')
pl_2 = Player('O')

while True:
    # __________________P1___________________________
    board.brd_displ()
    while True:  # choice_validator will ask continuosly for right input
        move = pl_1.choice()
        if board.choice_validator(move):
            board.fld_kill(move, pl_1.symb)
            pl_1.moves_reg(move)
            break
    if pl_1.win_check():
        break

    if board.draw():  # draw check
        break
    # __________________P2___________________________
    board.brd_displ()
    while True:
        move = pl_2.choice()
        if board.choice_validator(move):
            board.fld_kill(move, pl_2.symb)
            pl_2.moves_reg(move)
            break
    if pl_2.win_check():
        break

