
class Zaidejas:
    '''
    Klase nusako zaideja, o funkcijos tikrina ar jis laimejo
    '''
    def __init__(self, zenklas):
        self.zenklas = zenklas
        self.ejimu_str = ""
        self.laimejimimo_salygos = ["123", "456", "789", "147", "258", "369", "159", "753"]

    def zaidejo_pasirinkimas(self):
        '''
        Funkcija skirta zaidejo langelio pasirinkimui, kuris bus isrekstas kaip
        int, ir pasirinktu langeliu skaicu kaupimui kaip string
        :return:
        '''
        indeksas = int(input(f"Iveskite norimo pazymeti {self.zenklas} zenklu lauko numeri: "))
        self.ejimu_str += str(indeksas)
        return indeksas

    def laimejimo_tikrinimas(self):
        '''
        funkcija tikrina ar zaidejas turi susirinkes laimejimo kombinacija
        (galima laimeti turint stringe bet kurios laimejimo kombinacijos
        visus 3 skaicius) (Dvi istrizaines trys horizontales ir trys vertikales)
        Grazina True, jeigu stringe yra laimejimo kombinacija, arba False jei ne.

        :param ejimu_str: skaicius string tipo bet kokio ilgio
        :return: Bolean
        '''
        for numeris in self.laimejimimo_salygos: # pasirenkame is eiles laimingus skaicius(kombinacijas)
            laimejimo_skaicius = []
            counter = 0
            for skaiciukas in numeris: # numeri isskaidome i pavienius skaicius
                laimejimo_skaicius.append(skaiciukas) # prisegame pavieni skaiciu i laimejimo_skaiciu lista
                if skaiciukas in self.ejimu_str: # jei toks skaicius buvo pasirinktas tuomet pridesim counteri
                    counter += 1
                if counter == 3: # jei counteris pasieks 3 reiskia visi laimigo skaiciaus skaiciai, t.y pozicijos surinktos
                    print(f"{self.zenklas} zaidejas laimejo!") # ir eilute is 3 surinkta
                    return True
        return False
