numero1 = int(input("Digite um número inteiro: "))
numero2 = int(input("Digite o segundo número inteiro: "))
numero3 = int(input("Digite o último número inteiro: "))

numerosAntesDaOrdem = [
    numero1, numero2, numero3
]

numerosArrumados = numerosAntesDaOrdem.sort(reverse=True)

print(f"essa é sua ordem: {numerosAntesDaOrdem}")


## modo 2 


for numero in range(len(numerosAntesDaOrdem)):
    for j in range(len(numerosAntesDaOrdem) - 1):
        if numerosAntesDaOrdem[j] < numerosAntesDaOrdem[j + 1]:
            numerosAntesDaOrdem[j], numerosAntesDaOrdem[j + 1] = numerosAntesDaOrdem[j + 1], numerosAntesDaOrdem[j]
            
print(numerosAntesDaOrdem)
