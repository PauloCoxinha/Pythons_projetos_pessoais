precos = [
    ('D', float('-inf'), 50, 200),
    ('D', 51, 853, 120),
    ('N', float('-inf'), 50, 100),
    ('N', 51, 853, 80)
    ]

tipodevoo = input("Qual é o tipo de voo? D ou N: ").upper()
passageiros = int(input("Quantos passageiros estão a bordo? "))

for tipo, quantidade, quantidade2, preco in precos:
    if quantidade <= passageiros <= quantidade2 and tipodevoo == 'D':
        total = quantidade * preco

        print(f"O total a se pagar é: {total}")
    
    elif quantidade <= passageiros <= quantidade2 and tipodevoo == 'N':
        total = quantidade * preco
        print(f"O total a se pagar é: {total}")
