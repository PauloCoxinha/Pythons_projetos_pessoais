saldo = float(input("Digite o seu saldo médio: "))

valorfinal = 0

porcentagem = 0

margens = [
    (float('-inf'), 2000.00, 0.10),
    (2000.01, 3000.00, 0.20),
    (3000.01, 4000.00, 0.25),
    (4000.01, float('inf'), 0.30)
]       

for min, maximo, porc in margens:
    if min <= saldo <= maximo:
        porcentagem = saldo * porc
        


        #MANO EU N SEI OQ ACONTECEU MAS O CÓDIGO QUEBROU

        print(f"O seu valor de crédito é de: {porcentagem:.2f}")


#receba o gap mano, n vouu perder a streak nem tenta



