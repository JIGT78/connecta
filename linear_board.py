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
        # siempre y cuando no esté lleno...
        if not self.is_full:
            # buscamos la primera posición libre (None)
            i = self._column.index(None)
            # lo sustituimos por char
            self._column[i] = char

    def is_full(self):
        # comprobamos si esta llena la ultima posición
        return self._column[-1] != None

    def is_victory(self, char):

        """
        TODO implementar correctamente esta función
        """
        is_char = False
        counter = 0

        while(is_char==False and counter < BOARD_LENGTH):
            if (self._column[counter] == char):
                is_char = True
            counter=+1

        return is_char

        """
        1. Detectaremos la presencia de UNA instancia del elemento 
        dentro de una lista, en cualquier posición

        is_char = false

        for i in range(BOARD_LENGTH-1):
            if i == char:
                is_char = True

        2. Detectaremos la presencia de N instancias del elemento 
        dentro de una lista, en cualquier posición

        counter = 0

        for i in range(BOARD_LENGTH-1):
            if i == char:
                counter =+ 1

        3. Detectaremos la presencia de N instancias SEGUIDAS 
        del elemento dentro de una lista

        """
        prevPosition = None
        counter = 0

        for i in range(BOARD_LENGTH-1):
            if i == 0 and i == char:
                counter =+ 1
            elif i == char and prevPosition == char:
                counter =+ 1
            prevPosition = i
        


    def is_tie(self, char1, char2):
        """
        no hay victoria ni de char1 ni de char2
        """
        return (self.is_victory('x') == False) and (self.is_victory('o') == False)