
# todo 1. Leistų žaisti dviems žaidėjams (X ir O).
# todo 2. Teisingai fiksuotų žaidėjo laimėjimą ir stabdytų žaidimą
# Suformuoti zaidimo laukus

veiksmo_laukas = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
laimejimo_skaiciai = ["123", "456", "789", "147", "258", "369", "159", "753"]
X_laukai = []
O_laukai = []

print(veiksmo_laukas[7:10])
print(veiksmo_laukas[4:7])
print(veiksmo_laukas[1:4])

# Suformuoti ivedimo mechanzma
for _ in range(9):
    X_indeksas = int(input("Iveskite norimo pazymeti 'X' zenklu lauko numeri: ")) # Zaidejas pasirenka langeli
    X_laukai.append(str(X_indeksas))
    O_indeksas = int(input("Iveskite norimo pazymeti 'O' zenklu lauko numeri: ")) # Zaidejas pasirenka langeli
    O_laukai.append(str(O_indeksas))




# todo  3. Žaidimas vyktų konsolėje, grafinio interfeiso nereikia (bet galima daryti, tada konsolės nebereikia)
# todo  4. Sukurtą žaidimą paskelbti github repozitorijoje, nuorodą paskelbti teamsuose,
#           tam skirtoje užduotyje (Assignments)