#verificar se o usuário pode comprar pão e quantos pães ele consegue

pao = 2.00

decisao = input("Você vai querer comprar pão? ")

if decisao == "sim":
    pergunta_money = float(input("Quanto de dinheiro você tem? "))
    if pergunta_money >= pao:
        quantidade = pergunta_money / pao
        quantidade = int(quantidade)
        print(f"Você pode comprar {quantidade} de pães")
        
elif decisao == "não":
    print("ent vaza otariokkkkkk")   


# verificar a temperatura

temperatura = int(input("quantos graus está fazendo ai?"))


if temperatura < 0:
    print(f"Viado tu tá no alasca sai dai, {temperatura} graus não é pra qualquer um")

elif temperatura < 10:
    print(f"Tá bem frio ai né pra fazer {temperatura} graus")

elif temperatura < 20:
    print(f"Tá suave ai, {temperatura} graus é fichinha")

elif temperatura < 30:
    print(f"{temperatura} GRAUS?? ISSO AI TA MT QUENTE")

else:
    print("SAI DAI, SE NÃO VC VAI MORRER DE TANTO CALOR")