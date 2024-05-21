def find_one(list, needle):
    """
    Devuelve True si encuentra una o más ocurrencias de needle en list
    """
    return find_n(list, needle,1)

def find_n(list, needle, n):
    """
    Devuelve True si en list hay n o más ocurrencias de needle
    False si hay menos o si n < 0
    """
    # si n >= 0 ...
    if n >= 0 :
        # Inicializamos el índice y el contador
        index = 0
        count = 0

        # mientras no hayamos encontrado al elemento n veces o no hayamos terminado la lista...
        while count < n and index < len(list):
                # si lo encontramos, actualizamos el contador
                if needle == list[index]:
                     count = count + 1
                # avanzamos al siguiente elemento
                index = index + 1
        # devolvemos el resultado de comparar contador con n
        return count >= n
    else:
         return False