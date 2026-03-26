frutas = ["banana", "pera", "maça", "uva"]

for f in frutas:
    print(f)

nome = "Paulo"

for letra in nome:
    print(letra)


contador = 0 

while contador <= 10:
    print(f"O contador está em {contador}")
    contador += 1


numero = [1, 4, 6, 3, 2, 7, 9]

for n in numero:
    if n % 2 != 0:
        continue    
    print(f"O número {n} é par")


dados = {'Nome': "Paulo", "Inscritos": 1300, "categoria": "Self improvement"}

for c in dados.keys():
    print(f"{c}")