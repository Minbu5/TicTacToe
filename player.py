from colorama import Fore, Style
class Player:
    """
    Is to define player, and he's actions
    during game
    """

    def __init__(self, symb="*"):
        self.symb = symb
        self.moves_str = ""
        self.win_cond = ["123", "456", "789", "147", "258", "369", "159", "753"]

    def choice(self):
        """
        For player choice input.
        :return: str
        """
        choice = input(f"Iveskite norimo pažymėti {self.symb} ženklu lauko numerį: ")
        return choice

    def moves_reg(self, move):
        """ Registers moves. Move here is an integer"""
        self.moves_str += str(move)

    def win_check(self):
        """
        Checks if player reached wining coditions.
        - Has any 3 digits from win_cond list.
        - win_cond digits list represents 2 diagonals, 3 verticals and 3 horizontals
        - Returns True if wining reached or False if not

        :return: boolean
        """
        for num in self.win_cond:  # takes wining combination from list win_cond
            win_numb = []
            counter = 0
            for dig in num:  # split this comb into single digits
                win_numb.append(dig)  # append digit to new list for compare
                if dig in self.moves_str:  # if we have this number in moves, than we count
                    counter += 1
                if counter == 3:  # when counter reaches 3 this means we have winnig number in our moves
                    # print(f"{self.symb} zaidejas laimejo!")
                    return True
        return False
