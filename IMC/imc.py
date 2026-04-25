import tkinter as tk

peso = float(input("Digite o seu peso (apenas números): "))
altura = float(input("Digite sua altura (apenas números): "))

imcAltura = altura * altura

imc = peso / imcAltura

if imc < 18.5:
    print("Você está com magreza")  
elif imc > 18.5 and imc <= 24.9:
    print("Você está com um peso totalmente normal")
elif imc > 25 and imc < 30:
    print("Você está com sobrepeso")
elif imc > 30 and imc < 35:
    print("Você está com grau de obesidade 2")
else:
    print("Você está com obsediade mórbida")