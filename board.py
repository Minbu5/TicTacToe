class Tboard:
    """Class defines board usage by the game rules"""
    def __init__(self):
        self.flds = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
        self.max_moves = 0
        self.intro = "Jus sveikina kryziukai ir nuliukai zaidimas(TicTacToe)\n" \
                     "Noredami pasirinkti laukeli spauskite atitinkama skaiciu klaviaturoje"

    def brd_displ(self):
        """Function shows board in console
        :return None"""
        # spauzdina 3 masyvus
        print(self.flds[7:10])
        print(self.flds[4:7])
        print(self.flds[1:4])

    def fld_kill(self, choice, symb):

        """Function managing chosen field:
        - change field digit to player symbol
        - marks this field as used
        - counts moves for draw outcome

        :return: None
        """
        self.flds[int(choice)] = symb
        self.max_moves += 1

    def draw(self):
        """
        Checks if draw coditions are met (max moves 9)
        If draw True, otherwise False
        :return: boolean
        """
        if self.max_moves == 9:
            print("Lygiosios.")
            return True
        return False

    def choice_validator(self, choice):
        """ Function to check if player choice is valid.
         Checks for:
         1. choice is not string
         2. choice is number from 1-9 range
         3. choice is not repeated
         :return: boolean
         """
        try:
            choice = int(choice)
            if 0 < choice < 10:
                if choice in self.flds:
                    return True
                else:
                    print(f"Langelis: {choice} jau uzimtas. Rinkites kita.")
                    return False
            else:
                print(f"Toks pasirinkimas ({choice}) negalimas! Galima rinktis tik skaiciu nuo 1 iki 9")
                return False
        except ValueError:
             print("Toks pasirinkimas (raides) negalimas! Galima rinktis tik skaiciu nuo 1 iki 9")
             return False

