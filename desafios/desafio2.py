def narcissistic(value):
    valueString = str(value)
    digitos = [int(d) for d in valueString]
    valores_len = len(valueString)
    lista_da_ope = []
    for numero in digitos:
        lista_da_ope.append(numero ** valores_len)
        soma = sum(lista_da_ope)
    if soma == value:
        return True
    else:
        return False