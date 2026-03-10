numeros = [1, 2, 3, 4]
numeros.append(6)
numeros.remove(2)

posicao = numeros.index(4)

numeros.insert(posicao, 40)
numeros.remove(4)
print(numeros)

numeros.sort(reverse=True)

print(numeros)

frutas = ("Maçã", "Banana", "Laranja", "Uva")
if "Banana" in frutas:
    print("Banana está nas frutas")

frutas_lista = list(frutas)
frutas_lista.append("Abacaxi")
frutas_lista2 = tuple(frutas_lista)

print(frutas_lista2)

aluno = {'nome': 'Maria', 'Idade': 20, 'curso': 'engenharia'}
aluno['nota'] = 9.5
aluno['Idade'] = 21

print(aluno)
aluno.pop('curso') 
aluno['cursos'] = ['Engenharia', 'Medicina', 'OnlyFans']

print(aluno)

