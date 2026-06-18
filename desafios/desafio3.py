from math import sqrt

def find_next_square(sq):
    indice = 0
    raiz = sqrt(sq)
    if isinstance(raiz, (int, float)) and raiz.is_integer():
        raiz = raiz + 1
        indice = raiz 
        return indice ** 2 
    else:
        return -1



    
    