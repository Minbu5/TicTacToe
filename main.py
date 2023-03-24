
# todo 1. Leistų žaisti dviems žaidėjams (X ir O).

# Suformuoti zaidimo laukus
veiksmo_laukas = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
laimejimimo_salygos = ["123", "456", "789", "147", "258", "369", "159", "753",]

X_laukai_laimejimui = []
O_laukai_laimejimui = []
X_eimu_str = ""
O_eimu_str = ""

# X_eimu_str = "1936"
# for numeris in laimejimimo_salygos:
#     laimingas_skaicius = []
#     counter = 0
#     for skaiciukas  in numeris:
#         laimingas_skaicius.append(skaiciukas)
#         if skaiciukas in X_eimu_str:
#             counter += 1
#     if counter == 3:
#         print("Winner")
#     # print(laimingas_skaicius)


print(veiksmo_laukas[7:10])
print(veiksmo_laukas[4:7])
print(veiksmo_laukas[1:4])

# Suformuoti ivedimo mechanzma
for _ in range(9):
    # X zaidejas
    X_indeksas = int(input("Iveskite norimo pazymeti 'X' zenklu lauko numeri: ")) # Zaidejas pasirenka langeli
    X_laukai_laimejimui.append(str(X_indeksas))
    veiksmo_laukas[X_indeksas] = "X"
    X_eimu_str += str(X_indeksas)
    print(veiksmo_laukas[7:10])
    print(veiksmo_laukas[4:7])
    print(veiksmo_laukas[1:4])
    # laimejimo tikrinimas

    for numeris in laimejimimo_salygos:
        laimingas_skaicius = []
        counter = 0
        for skaiciukas in numeris:
            laimingas_skaicius.append(skaiciukas)
            if skaiciukas in X_eimu_str:
                counter += 1
        if counter == 3:
            print("X player is Winner!")

    # O zaidejas

    O_indeksas = int(input("Iveskite norimo pazymeti 'O' zenklu lauko numeri: ")) # Zaidejas pasirenka langeli
    O_laukai_laimejimui.append(str(O_indeksas))
    veiksmo_laukas[O_indeksas] = "O"
    O_eimu_str += str(O_indeksas)

    print(veiksmo_laukas[7:10])
    print(veiksmo_laukas[4:7])
    print(veiksmo_laukas[1:4])

    # laimejimo tikrinimas

    for numeris in laimejimimo_salygos:
        laimingas_skaicius = []
        counter = 0
        for skaiciukas in numeris:
            laimingas_skaicius.append(skaiciukas)
            if skaiciukas in O_eimu_str:
                counter += 1
        if counter == 3:
            print("O player is Winner!")

# todo 2. Teisingai fiksuotų žaidėjo laimėjimą ir stabdytų žaidimą
# todo  3. Žaidimas vyktų konsolėje, grafinio interfeiso nereikia (bet galima daryti, tada konsolės nebereikia)
# todo  4. Sukurtą žaidimą paskelbti github repozitorijoje, nuorodą paskelbti teamsuose,
#           tam skirtoje užduotyje (Assignments)