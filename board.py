# todo 1. Leistų žaisti dviems žaidėjams (X ir O).
class Lenta:
    '''Klase nustato lentos veikima'''

    def __init__(self):
        self.veiksmo_laukas = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
        self.max_ejimu = 0
        self.intro = "Jus sveikina kryziukai ir nuliukai zaidimas(TicTacToe)\n" \
                     "Noredami pasirinkti laukeli spauskite atitinkama skaiciu klaviaturoje"


    def veiksmo_lauko_vaizdavimas(self):
        '''
        Funkcija vaizduoja lauka
        :return: None
        '''
        # spauzdina 3 masyvus
        print(self.veiksmo_laukas[7:10])
        print(self.veiksmo_laukas[4:7])
        print(self.veiksmo_laukas[1:4])


    def laukelio_keitimas(self, indeksas, zenklas):

        '''Funkcija keicia laukeli matricoje zaidejo zenklu'''
        self.veiksmo_laukas[indeksas] = zenklas
        self.max_ejimu += 1


    def lygiosios(self):
        '''
        funkcija tikrina ar pasiektas maximalus ejimu skaicius(9).
        Jei pasiektas grazina True, jei ne False.
        :return: Bolean
        '''
        if self.max_ejimu == 9:
            print("Lygiosios.")
            return True
        return False


