#try:
 #   n1 = int(input("Digite um numero: "))
  #  n2 = int(input("Digite um outro numero: "))
#
 #   resultado = n1 + n2 
#
 #   print(f"Aqui está o seu resultado {resultado}")
#except Exception as erro:
 #   print("Digite um número seu babaca")

# try:
#    numero = float(input("Digite um numero: "))
#    resultado = 10 / numero
   
# except ValueError as error:
#    print(f"Erro ocorrido: {error}")
# except ZeroDivisionError as error:
#    print(f"Erro ocorrido! {error}")
# else:
#    print(f"O resultado é {resultado}")
# finally:
#    print("Fim do calculo rapaz")

# try:
#     frutas = ["Maça", "Pera", "Banana"]

#     print(frutas[3])
# except IndexError as error:
#     print(f"Selecionamos uma fruta que não existe e por isso deu {error}")

try:
    idade = int(input("Qual a sua idade? "))
    if idade < 0:
        raise ValueError("Digite um idade válida")
except Exception as erro:
    print(f"Erro: {erro}")
else:
    print(f"Sua idade é: {idade}")

