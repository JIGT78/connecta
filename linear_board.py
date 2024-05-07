from  settings import BOARD_LENGTH, VICTORY_STRIKE

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
        # buscamos la primera posición libre (None)
        i = self._column.index(None)
        # lo sustituimos por char
        if not is_full():
            self._column[i] = char

    def is_full(self):
        is_full = None
        for i in self._column.__le__ -1:
            # contamos las posiciones llenas y si coincide con la longitud  is_full true

    def is_victory(self, char):
        return False
    
    def is_tie(self, char1, char2):
        return False