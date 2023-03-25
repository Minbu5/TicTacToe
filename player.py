class Zaidejas:
    '''
    Klase nusako zaideja, o funkcijos leidzia pasirinkti langeli
    ir seka ar zaidejas laimejo
    '''

    def __init__(self, zenklas):
        self.zenklas = zenklas
        self.ejimu_str = ""
        self.laimejimimo_salygos = ["123", "456", "789", "147", "258", "369", "159", "753"]


# todo  Tikrintu ar nepasirinktas simbolis(raide).
    def zaidejo_pasirinkimas(self):
        '''
        Funkcija skirta zaidejo langelio pasirinkimui, kuris bus isrekstas kaip
        int, ir pasirinktu langeliu skaicu kaupimui kaip string

        :return: int
        '''
        klausti = True
        while klausti:
            try:
                indeksas = int(input(f"Iveskite norimo pazymeti {self.zenklas} zenklu lauko numeri: "))
                if 0 < indeksas < 10:
                    self.ejimu_str += str(indeksas)
                    klausti = False
                    return indeksas
                else:
                    print(f"Toks pasirinkimas ({indeksas}) negalimas! Galima rinktis tik skaiciu nuo 1 iki 9")

            except ValueError:
                print("Toks pasirinkimas (raides) negalimas! Galima rinktis tik skaiciu nuo 1 iki 9")



    def laimejimo_tikrinimas(self):
        '''
        funkcija tikrina ar zaidejas turi susirinkes laimejimo kombinacija
        (galima laimeti turint stringe bet kurios laimejimo kombinacijos
        visus 3 skaicius) (Dvi istrizaines trys horizontales ir trys vertikales)
        Grazina True, jeigu stringe yra laimejimo kombinacija, arba False jei ne.

        :return: Bolean
        '''
        for numeris in self.laimejimimo_salygos:  # pasirenkame is eiles laimingus skaicius(kombinacijas)
            laimejimo_skaicius = []
            counter = 0
            for skaiciukas in numeris:  # numeri isskaidome i pavienius skaicius
                laimejimo_skaicius.append(skaiciukas)  # prisegame pavieni skaiciu i laimejimo_skaiciu lista
                if skaiciukas in self.ejimu_str:  # jei toks skaicius buvo pasirinktas tuomet pridesim counteri
                    counter += 1
                if counter == 3:  # jei counteris pasieks 3 reiskia visi laimigo skaiciaus skaiciai, t.y pozicijos surinktos
                    print(f"{self.zenklas} zaidejas laimejo!")  # ir eilute is 3 surinkta
                    return True
        return False
