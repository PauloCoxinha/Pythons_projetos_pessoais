numero1 = int(input("Digite um número: "))
numero2 = int(input("Digite um número: "))
numero3 = int(input("Digite um número: "))



numeros = [
    numero1, numero2, numero3
]

numeroMaior = numeros[0]

numeros.sort(reverse=True)

print(numeros[0])   

for numero in numeros:
    if numero >= numeroMaior:
        numeroMaior = numero
        print(numeroMaior)




print(max(numero1, numero2, numero3))
    