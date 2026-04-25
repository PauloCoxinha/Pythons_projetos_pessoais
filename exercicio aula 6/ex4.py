preços = [
    ('D', float('-inf'), 50, 200),
    ('D', 51, 853, 120),
    ('N', float('-inf'), 50, 100),
    ('N', 51, 853, 80)
    ]

tipodevoo = input("Qual é o tipo de voo? D ou N: ").upper()
passageiros = int(input("Quantos passageiros estão a bordo? "))

for tipo, quantidade, quantidade2, preço in preços:
    if quantidade <= passageiros <= quantidade2 and tipo == tipodevoo:
        total = passageiros * preço
        print(f"O total da tarifa é: {preço}")
        print(f"O total a se pagar é: {total}")
    
      
