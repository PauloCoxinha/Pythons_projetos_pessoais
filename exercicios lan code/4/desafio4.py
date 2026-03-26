contador = 0

while contador <= 10:
    print(contador)
    contador += 1


index = 1

numero = int(input("Insira um número para a tabuada: "))



while index < 11:
    tabuada = index * numero
    print(f"{numero} X {index} = {tabuada}")
    index += 1


palavra = input("Digite algo: ")
palavra_index = 0

for letra in palavra:
    if letra in 'a, e, i, o, u':
     palavra_index += 1
     
print(f"sua palavra tem {palavra_index} vogais")




index_tabuada = 1

numerotabu = 1

while index_tabuada < 101:
   while numerotabu < 11:
    tabuada2 = index_tabuada * numerotabu
    print(f"{index_tabuada} X {numerotabu} = {tabuada2}")
    numerotabu += 1
   index_tabuada += 1
   numerotabu = 1 



#forma do chat gpt resolver a baixo

for numero in range(1, 101):
    for multiplicador in range(1, 11):
        resultado = numero * multiplicador
        print(f"{numero} x {multiplicador} = {resultado}")
        
