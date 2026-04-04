tempo = int(input("Quantos dias voce passou no hospital? "))
quarto_tempo = input("e que tipo de quarto voce dormiu? SP, P, C ").upper()
wifi = input("Você usou wi-fi? sim ou não? ")
tv = input("E tv a cabo? sim ou não? ")

wifi_preco = 4

tv_preco = 4

quartos = {
    'P': 360,
    'SP': 210,
    'C': 185
}


valor_real = quartos[quarto_tempo]

operacao = tempo * valor_real
if wifi == 'sim' and tv == 'sim':
    soma = wifi_preco + tv_preco
    total = operacao + soma
elif wifi == 'não' and tv == 'sim':
     soma = tv_preco
     total = operacao + soma
elif wifi == 'sim' and tv == 'não':
     soma = wifi_preco
     total = operacao + soma
else:
     soma = 0
     total = operacao + soma


print(f"Sua conta é de {total}")

