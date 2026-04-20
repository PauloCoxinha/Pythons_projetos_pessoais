a = float(input("Digite o valor de a: "))

b = float(input("Digite o valor de b: "))

c = float(input("Digite o valor de c: "))

triangulo = False


if a + b > c and a + c > b and b + c > a:
    triangulo = True
    if a == b == c:
        tipoDeTriangulo = 'Triangulo Equilatero'
        print(tipoDeTriangulo)
    elif a == b or a == c or b == c:
        tipoDeTriangulo = 'Triangulo Isosceles'
        print(tipoDeTriangulo)
    elif a != b and a != c and b != c:
        tipoDeTriangulo = 'Triangulo Escaleno'
        print(tipoDeTriangulo)
else:
    print("Não pode ser triangulo")
def trianguloReal(valor1, valor2, valor3):
    triangulo = False
    if valor1 + valor2 > valor3 and valor1 + valor3 > valor2 and valor2 + valor3 > valor1:
        triangulo = True
        if valor1 == valor2 == valor3:
            tipoDeTriangulo = 'Triangulo Equilatero'
            print(tipoDeTriangulo)
        elif valor1 == valor2 or valor1 == valor3 or valor2 == valor3:
            tipoDeTriangulo = 'Triangulo Isosceles'
            print(tipoDeTriangulo)
        elif valor1 != valor2 and valor1 != valor3 and valor2 != valor3:
            tipoDeTriangulo = 'Triangulo Escaleno'
            print(tipoDeTriangulo)
    else:
        print("Não pode ser triangulo")