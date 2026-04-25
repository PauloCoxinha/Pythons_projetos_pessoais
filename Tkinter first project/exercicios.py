print("Olá estou aprendendo python")

nome = input("Qual é o seu nome?")

idade = int(input("Qual a sua idade?"))

print(f"Olá {nome} eu sei que voce tem {idade} anos")


n1 = int(input("Me diz um número "))

n2 = int(input("Me diz outro número "))

soma = n1 + n2 

def subtracao(a, b):
    if a >= b:
        return a - b
    else:
        return b - a
    
resultado_sub = subtracao(n1, n2)

print(f"o resultado da somas dos seus números é {soma} e subtração é {resultado_sub}")