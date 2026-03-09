def somar(n1, n2):
    resultado = n1 + n2
    return resultado



resultado_da_soma = somar(232, 324)
print(resultado_da_soma)
resultado_de_outra_soma = somar(2323234, 2301302103210)
print(resultado_de_outra_soma)




def verificar_par(n):
    if n % 2 == 0:
        return True
    else:
        return False

numero = int(input("Digite um número "))


if verificar_par(numero):
    print("é par")
else: 
    print("é impar")


def somar2(*numeros):
    resultado = 0
    for numero in numeros:
        resultado += numero
    return resultado



resultado_da_lista = somar2(2, 4, 5, 4, 6, 87, 435)
print(resultado_da_lista)

def calcular_media(*numeros):
    qnt = len(numeros)
    soma = 0
    for numero in numeros:
        soma += numero
    media = soma / qnt
    return media

resultado = calcular_media(3, 4, 10, 8, 9, 8, 2, 1)

print(resultado)


def informacoes_pessoais(**informacoes):
    for chave, valor in informacoes.items():
        print(f"{chave}: {valor}")

informacoes_pessoais(nome= 'Paulo', idade= 20, curso='ADS')
