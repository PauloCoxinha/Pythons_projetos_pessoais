import json 

json_string = """{

"personas": [ 
{
"nome": "João",
"idade": 22,
"cidade": "São_Paulo",
"profissao": "Engenheiro"
},
{
"nome": "João",
"idade": 22,
"cidade": "São_Paulo",
"profissao": "padeiro"
},
{
"nome": "João",
"idade": 22,
"cidade": "São_Paulo",
"profissao": "metaleiro"
}
]}"""

dados = json.loads(json_string)


for pessoa in dados['personas']:
    nome = pessoa['nome']
    idade = pessoa['idade']
    cidade = pessoa['cidade']
    profissao = pessoa['profissao']

<<<<<<< HEAD
    print(f"\n nome: {nome} \n idade: {idade} \n cidade: {cidade} \n profissao: {profissao} ")
=======
    print(f"\n nome: {nome} \n idade: {idade} \n cidade: {cidade} \n profissao: {profissao} ")


cachorro = {
    "raça": 'Husk',
    "idade": 2,
    "dono": "Paulo",
    "país": "Canadá"
}

json_cachorro = json.dumps(cachorro)

print(type(json_cachorro))
print(type(dados))




with open('frutas.json', 'r', encoding='utf-8') as arq:
    dadosreais = json.load(arq)
    print(dadosreais)
>>>>>>> 2afd836636c466b662a99b9de46bcb7b84c9ef9c
