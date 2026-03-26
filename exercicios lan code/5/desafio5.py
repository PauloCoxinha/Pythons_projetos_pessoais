numero = int(input("Digite um número"))

def contador(n):
    while n > 0:
        print(n)
        n -= 1

contagem = contador(numero)




def maior_numero(lista_de_numeros):
    maior_numero = lista_de_numeros[0]
    for numero in lista_de_numeros:
        if numero > maior_numero:
            maior_numero =  numero
    return maior_numero
    
numeros_inteiros = [3, 5, 10, 32, 34, 2, 90, 40]
maior_numero_da_lista = maior_numero(numeros_inteiros)

print(f"O maior número da lista é {maior_numero_da_lista}")