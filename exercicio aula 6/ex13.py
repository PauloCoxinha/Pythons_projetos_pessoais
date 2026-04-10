import math

print("Os valores que vão ser digitados a seguir tem como referência uma equação de 2 grau")
a = float(input("Digite um número real: "))
b = float(input("Digite outro número real: "))
c = float(input("Ultimo numero real"))

if a == 0:
    print(f"Não pode ser equação de segundo grau")




def delta1():
    bQuadrado = b ** 2 
    delta = bQuadrado - 4 * a * c 
    if delta < 0:
        print(f"O valor do delta é {delta} então ele não é um valor real e não pode ser considerado")
    else: 
        print(f"O valor de delta é {delta}")
        return delta

def delta2(aa, bb, cc):
    bQuadrado = bb ** 2 
    delta = bQuadrado - 4 * aa * cc
    if delta < 0:
        print(f"O valor do delta é {delta} então ele não é um valor real e não pode ser considerado")
    else: 
        print(f"O valor de delta é {delta}")
        return delta

d = delta2(a, b, c)

x1 = (-b + math.sqrt(d)) / (2 * a)

x2 = (-b - math.sqrt(d)) / (2 * a)

print(x1)

print(x2)
