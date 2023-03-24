# todo 1. Leistų žaisti dviems žaidėjams (X ir O).
class Lenta:
    def __init__(self):
        self.veiksmo_laukas = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
        self.laimejimimo_salygos = ["123", "456", "789", "147", "258", "369", "159", "753"]
        self.max_ejimu = 0
        self.zaidimas_vyksta = True

    def veiksmo_lauko_vaizdavimas(self, skaiciukas=1, zenkliukas='+'):
        '''
        Funkcija keicia skaiciu nurodytame indexe(skaiciukas int)
        i nurodyta simboli (zenkliukas str)
        :return: None
        '''
        # padavus lauko skaiciu:
        self.veiksmo_laukas[skaiciukas] = zenkliukas

        print(self.veiksmo_laukas[7:10])
        print(self.veiksmo_laukas[4:7])
        print(self.veiksmo_laukas[1:4])
        # spauzdina 3 masyvus

    def laimejimo_tikrinimas(self, ejimu_str):
        '''
        funkcija tikrina ar zaidejas turi susirinkes laimejimo kombinacija
        (galima laimeti turint stringe bet kurios laimejimo kombinacijos
        visus 3 skaicius) (Dvi istrizaines trys horizontales ir trys vertikales)
        Grazina False, jeigu stringe yra laimejimo kombinacija.

        :param ejimu_str: skaicius string tipo bet kokio ilgio
        :return: Bolean
        '''
        for numeris in self.laimejimimo_salygos:
            laimingas_skaicius = []
            counter = 0
            for skaiciukas in numeris:
                laimingas_skaicius.append(skaiciukas)
                if skaiciukas in ejimu_str:
                    counter += 1
            if counter == 3:
                self.zaidimas_vyksta = False
        return self.zaidimas_vyksta

    def Lygiosios(self):
        '''
        funkcija tikrina ar maximalus ejimu skaicius nevirsytas.
        Jei pasiektas grazina False.
        :return: Bolean
        '''
        if self.max_ejimu == 9:
            self.zaidimas_vyksta = False
        return self.zaidimas_vyksta



lenta = Lenta()
lenta.veiksmo_lauko_vaizdavimas()
print(lenta.laimejimo_tikrinimas("1930"))
print(lenta.veiksmo_laukas[1])

