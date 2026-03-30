valorx = int(input("Digite um número"))

x = 0

if valorx <= 1:
    x =  1
    print(f'{x}')
elif valorx > 1 and valorx <= 2:
    x = 2
    print(f'{x}')
elif valorx > 2 and valorx <= 3:
    x = valorx ** 2
    print(f'{x}')
elif valorx >= 3:
    x = valorx ** 3
    print(f'{x}')