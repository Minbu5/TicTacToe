
class Lenta:
    '''Klase nustato lentos veikima'''

    def __init__(self):
        self.veiksmo_laukas = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
        self.uzimti_langeliai = []
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
        # todo 1 sukurti uzimto langelio ivedimo salygos tikrinima
        # problema kad suklydus zaidejo vel butu prasoma inputo, o jis yra kitoje klaseje..
        # gal bandyti klase importuoti ir sukurus objekta kreiptis bet tada 2 zaidejai...

        '''Funkcija:
         1.keicia laukeli matricoje zaidejo zenklu
         2.skaiciuoja ejimus.

        '''
        self.veiksmo_laukas[indeksas] = zenklas
        self.uzimti_langeliai.append(indeksas) # prideda pasikart kontrolei
        self.max_ejimu += 1

    def uzimtas_langelis(self, indeksas):
        '''Funkcija tikrina ar toks langelis jau pasirinktas.
        Priima int
        :return boolean
        '''
        if indeksas in self.uzimti_langeliai:
            return True
        else:
            return False

    def lygiosios(self): # todo 2 Gal laukelio keitimas ir lygiosios apjungti i viena
        '''
        funkcija tikrina ar pasiektas maximalus ejimu skaicius(9).
        Jei pasiektas grazina True, jei ne False.
        :return: boolean
        '''
        if self.max_ejimu == 9:
            print("Lygiosios.")
            return True
        return False
