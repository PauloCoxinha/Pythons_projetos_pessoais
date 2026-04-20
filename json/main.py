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

    print(f"\n nome: {nome} \n idade: {idade} \n cidade: {cidade} \n profissao: {profissao} ")