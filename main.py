from board import Lenta
from player import Zaidejas

lenta = Lenta()
lenta.veiksmo_lauko_vaizdavimas() # sukuriame zaidimo erdve

zaid_1 = Zaidejas('X') # sukuriam pirma zaideja
zaid_2 = Zaidejas('O') # sukuriam antra zaideja

while True:
    lenta.laukelio_keitimas(zaid_1.zaidejo_pasirinkimas(), zaid_1.zenklas) # zaidejas zymi laukeli
    lenta.veiksmo_lauko_vaizdavimas() # parodoma lenta su zaidejo pazymejimu
    if zaid_1.laimejimo_tikrinimas(): # tikrinam ar zaidejas laimejo
        break
    elif lenta.lygiosios(): # tikriname ar lygiosios t.y. atlikta 9 ejimai
        break

    lenta.laukelio_keitimas(zaid_2.zaidejo_pasirinkimas(), zaid_2.zenklas) # zaidejas zymi laukeli
    lenta.veiksmo_lauko_vaizdavimas() # parodoma lenta su zaidejo pazymejimu
    if zaid_2.laimejimo_tikrinimas(): # tikrinam ar zaidejas laimejo
        break


