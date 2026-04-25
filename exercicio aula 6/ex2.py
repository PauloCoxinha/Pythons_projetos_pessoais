litros = int(input("Quantos litros você vai querer? "))

respostagasolina = input("Qual combustivel você vai querer? selecione d para diesel, a para alcool e g para gasolina: ")

combustivel = {
    'd': 3.6543,
    'a': 3.8997,
    'g': 4.4009
}

for chave, valor in combustivel.items():
    if chave == respostagasolina:
        resultado = valor * litros
        print(f"vai custar R${resultado:.2f}")