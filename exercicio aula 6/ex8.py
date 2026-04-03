tempo = int(input("Quantos dias voce passou no hospital? "))
quarto_tempo = input("e que tipo de quarto voce dormiu? SP, P, C ")
wifi = input("Você usou wi-fi? sim ou não?")
tv = input("E tv a cabo? sim ou não?")

wifi_preco = 4

tv_preco = 4

quartos = {
    'P': 360,
    'SP': 210,
    'C': 185
}

for chave, a in quartos:
    if chave == quarto_tempo:
        operacao = tempo * a 
        if wifi == 'sim' and tv == 'sim':
            soma = wifi_preco + tv_preco
            total = operacao + soma
            print(f"Sua conta é de {total}")

