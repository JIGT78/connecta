from  settings import BOARD_LENGTH, VICTORY_STRIKE
from list_utils import find_streak

class LinearBoard():
    """
    Clase que representa un tablero de una sola columna
    x un jugador
    o otro jugador
    None un espacion vacio"""

    def __init__(self):
       """
       Una lista de None
       """
       self._column = [None for i in range (BOARD_LENGTH)]

    def add(self, char):
        """
        Juega en la primera posición disponible
        """
        # siempre y cuando no esté lleno...
        if not self.is_full():
            # buscamos la primera posición libre (None)
            i = self._column.index(None)
            # lo sustituimos por char
            self._column[i] = char

    def is_full(self):
        # comprobamos si esta llena la ultima posición
        return self._column[-1] != None

    def is_victory(self, char):
        return find_streak(self._column, char, VICTORY_STRIKE)


    def is_tie(self, char1, char2):
        """
        no hay victoria ni de char1 ni de char2
        """
        return (self.is_victory('x') == False) and (self.is_victory('o') == False)