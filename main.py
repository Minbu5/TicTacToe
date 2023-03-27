from board import Tboard
from player import Player
from colorama import Fore, Style
from logo import x_win, o_win, draw

import os

board = Tboard()
pl_1 = Player(f"{Fore.BLUE}X{Style.RESET_ALL}")

pl_2 = Player(f"{Fore.YELLOW}O{Style.RESET_ALL}")

print(board.intro)
while True:
    # __________________P1___________________________
    board.brd_displ()
    while True:  # choice_validator will ask continuously for right input
        move = pl_1.choice()
        if board.choice_validator(move):
            board.fld_kill(move, pl_1.symb)
            pl_1.moves_reg(move)
            break
    if pl_1.win_check():  # winning check
        print(x_win)
        board.brd_displ()
        break


    if board.draw():  # draw check
        print(draw)
        board.brd_displ()
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
        print(o_win)
        board.brd_displ()
        break

