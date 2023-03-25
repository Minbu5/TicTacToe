from board import Lenta
from player import Zaidejas


lenta = Lenta() # sukuriame zaidimo erdve
lenta.veiksmo_lauko_vaizdavimas()

zaid_1 = Zaidejas('X') # sukuriam pirma zaideja
zaid_2 = Zaidejas('O') # sukuriam antra zaideja

#  todo 1. Leistų žaisti dviems žaidėjams (X ir O).
while True:
    lenta.laukelio_keitimas(zaid_1.zaidejo_pasirinkimas(), zaid_1.zenklas) # zaidejas zymi laukeli
    lenta.veiksmo_lauko_vaizdavimas() # parodoma lenta su zaidejo pazymejimu
    if zaid_1.laimejimo_tikrinimas(): # tikrinam ar zaidejas laimejo
        break
    elif lenta.lygiosios():
        break

    lenta.laukelio_keitimas(zaid_2.zaidejo_pasirinkimas(), zaid_2.zenklas) # zaidejas zymi laukeli
    lenta.veiksmo_lauko_vaizdavimas() # parodoma lenta su zaidejo pazymejimu
    if zaid_2.laimejimo_tikrinimas(): # tikrinam ar zaidejas laimejo
        break


# todo pasikartojimu ir netinkamu simboliu vedima apsauga uztikrinti per try except boarde!!


#
# # Kintamieji
# veiksmo_laukas = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
# laimejimimo_salygos = ["123", "456", "789", "147", "258", "369", "159", "753",]
# max_ejimu = 0
# Zaidimas_vyksta = True
# X_laukai_laimejimui = []
# O_laukai_laimejimui = []
# X_eimu_str = ""
# O_eimu_str = ""
#
# # Vaizdavimas
# print(veiksmo_laukas[7:10])
# print(veiksmo_laukas[4:7])
# print(veiksmo_laukas[1:4])
#
# # Zaidimo eiga
# while Zaidimas_vyksta and max_ejimu != 9: # Lygiuju salyga
#     # X zaidejas
#     X_indeksas = int(input("Iveskite norimo pazymeti 'X' zenklu lauko numeri: ")) # Zaidejas pasirenka langeli
#     max_ejimu += 1
#     X_laukai_laimejimui.append(str(X_indeksas))
#     veiksmo_laukas[X_indeksas] = "X"
#     X_eimu_str += str(X_indeksas)
#     print(veiksmo_laukas[7:10])
#     print(veiksmo_laukas[4:7])
#     print(veiksmo_laukas[1:4])
#     print(max_ejimu)
#
#     # X laimejimo tikrinimas
#     for numeris in laimejimimo_salygos:
#         laimingas_skaicius = []
#         counter = 0
#         for skaiciukas in numeris:
#             laimingas_skaicius.append(skaiciukas)
#             if skaiciukas in X_eimu_str:
#                 counter += 1
#         if counter == 3:
#             print("X player is Winner!")
#             Zaidimas_vyksta = False
#
#
#     # O zaidejas
#     O_indeksas = int(input("Iveskite norimo pazymeti 'O' zenklu lauko numeri: ")) # Zaidejas pasirenka langeli
#     max_ejimu += 1
#     O_laukai_laimejimui.append(str(O_indeksas))
#     veiksmo_laukas[O_indeksas] = "O"
#     O_eimu_str += str(O_indeksas)
#
#     print(veiksmo_laukas[7:10])
#     print(veiksmo_laukas[4:7])
#     print(veiksmo_laukas[1:4])
#     print(max_ejimu)
#
#     # O laimejimo tikrinimas
#     for numeris in laimejimimo_salygos:
#         laimingas_skaicius = []
#         counter = 0
#         for skaiciukas in numeris:
#             laimingas_skaicius.append(skaiciukas)
#             if skaiciukas in O_eimu_str:
#                 counter += 1
#         if counter == 3:
#             print("O player is Winner!")
#             Zaidimas_vyksta = False
# if max_ejimu == 9:
#     print(veiksmo_laukas[7:10])
#     print(veiksmo_laukas[4:7])
#     print(veiksmo_laukas[1:4])
#     print("Lygiosios")





# todo 2. Teisingai fiksuotų žaidėjo laimėjimą ir stabdytų žaidimą
# todo  3. Žaidimas vyktų konsolėje, grafinio interfeiso nereikia (bet galima daryti, tada konsolės nebereikia)
# todo  4. Sukurtą žaidimą paskelbti github repozitorijoje, nuorodą paskelbti teamsuose,
#           tam skirtoje užduotyje (Assignments)