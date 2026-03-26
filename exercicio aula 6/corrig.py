# print("\n ===Este é o requisitos minímos para ter sua CNH=== \n")
# print("Para ter sua CNH, você precisa ser maior de idade, ou seja, ter 18 anos ou mais. \n")
# print("Se você tem entre 15 e 17 anos, você pode ter uma CNH Junior, que é uma permissão especial para menores de idade. \n")
# print("Se você tem menos de 15 anos, você não poderá ter uma CNH \n")
# print("O valor da CNH A é de R$ 200,00 \n")
# print("O valor da CNH B é de R$ 300,00 \n")

# def calcular_cnh(idade_usuario):
#     if idade_usuario >= 18:
#         return "Senior"
#     elif idade_usuario >= 15:
#         return "Junior"
#     else:
#         return "Infantil"
# idade_usuario = int(input("Digite sua idade: "))
# tipo_cnh = calcular_cnh(idade_usuario)
# if idade_usuario < 15:
#     print("Desculpe, você não pode ter uma CNH.")
# elif idade_usuario >= 15 and idade_usuario < 18:
#     print("Você pode ter uma CNH Junior, que é uma permissão especial para menores de idade.")
# else:
#     print("Você pode ter uma CNH!")


print("\n ===Este é o requisitos minímos para ter sua CNH=== \n")
print("Para ter sua CNH, você precisa ser maior de idade, ou seja, ter 18 anos ou mais. \n")
print("Se você tem entre 15 e 17 anos, você pode ter uma CNH Junior, que é uma permissão especial para menores de idade. \n")
print("Se você tem menos de 15 anos, você não poderá ter uma CNH \n")
print("O valor da CNH A é de R$ 200,00 \n")
print("O valor da CNH B é de R$ 300,00 \n")


idades = [ (18, float('inf'), 'Senior'),
          (15, 17, 'Junior'),
          (float('-inf'), 14, 'n pode')
]

habilitacao = 0

idade = int(input("Digite sua idade"))

for min, maximo, cnh in idades:
    if min <= idade <= maximo:
        habilitacao = cnh

        print(cnh)
