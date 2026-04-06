escolha = input("Você quer a temperatura de Fahrenheit ou Celsius? Escreva F para Fahrenheit e C para celsius: ")

escolha_maiuscula = escolha.upper()
    

numero = int(input("Escreva uma temperatura (ela vai interpretada como Celsius, porém ela vai ser convertida caso você escolheu Fahrenheit): "))



def Fahrenheit():
    conversaoFah = numero * 1.8 + 32    

    return conversaoFah


if escolha_maiuscula == 'C':
    print(f"{numero}°c")

elif escolha_maiuscula == 'F':
    print(f"{Fahrenheit():.2f}°F")

else:
    print("Você deve estar se achando o sabichão por pular as instruções né")