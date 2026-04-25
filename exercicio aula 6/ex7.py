numero1 = int(input("Digite um número"))
numero2 = int(input("Digite outro número"))


def media (a, b):
    return (a + b) / 2

def diferenca(a, b):
    return a - b

def produto(a, b):
    return a * b

def divisao(a, b):
    if a or b == 0:
        print("Escreva um digito maior que 0")
    else:
        return a / b
    
operacoes = {
    1: media,
    2: diferenca,
    3: produto,
    4: divisao,
}


escolha = int(input("Escolha um número entre 1 e 4")) 
if escolha not in [1, 2, 3, 4]:
    print("Escolha um número válido")
else:
    resultado = operacoes.get(escolha) 
    print(f"O resultado da sua equação é: {resultado(numero1, numero2)}")




