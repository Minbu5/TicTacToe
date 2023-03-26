from board import Tboard
from player import Player

board = Tboard() # sukuriame zaidimo erdve

pl_1 = Player('X') # sukuriam pirma zaideja
pl_2 = Player('O') # sukuriam antra zaideja



while True:

    board.brd_displ()
    while True: # choice_validator will ask continuosly for right input
        move = pl_1.choice()
        if board.choice_validator(move):
            board.fld_kill(move, pl_1.symb)
            pl_1.moves_reg(move)
            break
    if pl_1.win_check():
        break

    if board.draw():
        break

    board.brd_displ()
    while True:
        move = pl_2.choice()
        if board.choice_validator(move):
            board.fld_kill(move, pl_2.symb)
            pl_2.moves_reg(move)
            break
    if pl_2.win_check():
        game_on = False

# while True:
#     Tboard.laukelio_keitimas(zaid_1.zaidejo_pasirinkimas(), zaid_1.zenklas) # Player1 zymi laukeli
#     Tboard.veiksmo_lauko_vaizdavimas() # parodoma Tboard su zaidejo pazymejimu
#     if zaid_1.laimejimo_tikrinimas(): # tikrinam ar Player1 laimejo
#         break
#
#     elif Tboard.lygiosios(): # tikriname ar lygiosios t.y. atlikta 9 ejimai
#         break
#
#     Tboard.laukelio_keitimas(zaid_2.zaidejo_pasirinkimas(), zaid_2.zenklas) # Player2 zymi laukeli
#     Tboard.veiksmo_lauko_vaizdavimas()  # parodoma Tboard su zaidejo pazymejimu
#
#     if zaid_2.laimejimo_tikrinimas(): # tikrinam ar Player2 laimejo
#             break


