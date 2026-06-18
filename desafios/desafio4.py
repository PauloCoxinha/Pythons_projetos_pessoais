total = 0 
quero_comprar = True

while quero_comprar:
    preco = float(input("Preço: "))
    total += preco
    opcao = input('Continuar S/N? ')
    if opcao != 's':
        quero_comprar == False
print(f"Total da compra ${total}")