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

def find_streak(list, needle, n):
     """
     Devuelve True si en list hay n o más needles seguidos
     False, para todo lo demas
     """
     # si n >= 0
     if n >= 0:
        # Inicializo el indice, el contador y el indicador de racha
        index = 0
        count = 0
        streak = False
        # Mientras no haya encontrado n seguidos en la lista no se haya acabado ...
        while count < n and index < len(list):
            # si lo encuentro, activo el indicador de rachas y actualizo el contador
            if needle == list[index]:
                 streak = True
                 count = count + 1              
            # si no lo encuentro, desactivo el indicador de racha y pongo a cero el contador
            else:
                 streak = False
                 count = 0
            # avanzo al siguiente elemento
            index = index + 1
        # devolvemos el resultado de comparar el contador con n SIEMPRE Y CUANDO estemos en racha
        return count >= n and streak
     else:
        # para valores de n < 0, no tiene sentido
        return False

def first_elements(list_of_lists):
     """
     Recibe una lista de listas y devuelve una lista
     con los primeros elementos de la original
     """
     return nth_elements(list_of_lists, 0)

def nth_elements(list_of_lists, n):
     """
     Recibe una lista de listas y devuelve una lista
     con los enésimos elementos de la original
     """
     result = []

     for list in list_of_lists:
               result.append(list[n])

     return result

def transpose(matrix):
     """
     Recibe una matriz y devuelve su transpuesta
     """
     # Creo una matriz vacía llamada transp
     # TODO comprobar que todas las listas recibidas tienen la misma longitud
     transp = []
     # Recorremos todas las columnas de la matriz original
     for n in range(len(matrix[0])):
          # extraigo los valores enésimos y se los encasqueto a transp
          transp.append(nth_elements(matrix, n))
     # devuelvo transp
     return transp

def displace(l, distance, filler=None):
     if distance == 0:
          return l
     elif distance > 0:
          filling = [filler] * distance
          res = filling + l
          res = res[:-distance]
          return res
     else:
          filling = [filler] * abs(distance)
          res = l + filling
          res = res[abs(distance):]
          return res

def displace_matrix(m, filler=None):
      # creamos una matriz vacía 
      d = []
      # por cada columna de la matriz original y la desplazamos su indice -1
      for i in range(len(m)): # damos por hecho que es una matriz (lista de listas) todas de la misma longitud
          # añadimos la columna desplazada a m
          d.append(displace(m[i], i-1, filler))
      # devolvemos m
      return d 

def reverse_list(l):
     return list(reversed(l))

def reverse_matrix(matrix):
     rm = []
     for col in matrix:
          rm.append(reverse_list(col))
     return rm