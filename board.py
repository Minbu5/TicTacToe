from prettytable import PrettyTable, prettytable
from colorama import Fore, Style
from logo import logo

class Tboard:
    """Defines board usage by the game rules"""

    def __init__(self):
        self.flds = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
        self.max_moves = 0
        self.intro = logo

    def brd_displ(self):
        """Shows board in console

        :return None"""
        # split flds to 3 lists for pretty table data rows
        row1 = []
        row2 = []
        row3 = []
        for dig in self.flds[::-1]:
            if len(row1) < 3:
                row1.append(dig)
            elif len(row2) < 3:
                row2.append(dig)
            elif len(row3) < 3:
                row3.append(dig)
        tbl1 = PrettyTable()
        tbl1.header = False
        tbl1.add_row(row1[::-1])
        tbl1.add_row(row2[::-1])
        tbl1.add_row(row3[::-1])
        tbl1.hrules = prettytable.ALL
        print(tbl1)

    def fld_kill(self, choice, symb):

        """Managing chosen field:
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
        """ To check if player choice is valid and print
        corresponding error.
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
                    print(f"Langelis {Fore.RED}{choice}{Style.RESET_ALL} jau užimtas. Rinkitės kitą.")
                    return False
            else:
                print(f"Toks pasirinkimas ({Fore.RED}{choice}{Style.RESET_ALL}) nėra galimas! Rinktės skaicių nuo 1 iki 9")
                return False
        except ValueError:
            print(f"Toks pasirinkimas ({Fore.RED}raides, simboliai{Style.RESET_ALL}) nėra galimas! Rinktės skaicių nuo 1 iki 9")
            return False
