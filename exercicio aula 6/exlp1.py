pergunta = input('Quer adicionar algum produto? (responda com sim ou não) ').lower()
contador = 0

while pergunta == 'sim':
    produto = float(input('Digite o valor do produto que vocÊ comprou: '))
    contador = produto + contador
    pergunta = input('Quer adicionar algum produto? (responda com sim ou não) ').lower()

print(f'o valor das suas compras é de: {contador:.2f}')





