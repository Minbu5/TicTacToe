
class Zaidejas:
    def __init__(self, zenklas='X'):
        self.zenklas = zenklas
        self.laukai_laimejimui = []
        self.ejimu_str = ""

    def zaidejo_langelis(self):
        indeksas = int(input("Iveskite norimo pazymeti 'X' zenklu lauko numeri: "))
        # grazina numeriuka
        self.laukai_laimejimui.append(str(indeksas))
        self.veiksmo_laukas[indeksas] = "X"
        self.ejimu_str += str(indeksas)
    def laimejimo_laukai(self):
        pass



pl1 = Zaidejas()
print(pl1.zaidejo_ejimas())

