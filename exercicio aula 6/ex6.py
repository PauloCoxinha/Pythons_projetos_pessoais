peso = float(input("Digite o seu peso: "))
altura = float(input("Digite sua altura em cm: ")) / 100 

resultado = peso / (altura ** 2)

imc_medidas = [
    (float('-inf'), 18.9, 'Abaixo do peso'),
    (18.9, 24.9, 'normal'),
    (24.9, 29.9, 'excesso de peso'),
    (29.9, 34.9, 'obesidade'),
    (34.9, float('inf'), 'Obesidade mórbida'),   
]

for minimo, maximo, categoria in imc_medidas:
    if minimo <= resultado <= maximo:
        print(f'Sua categoria é: {categoria}')