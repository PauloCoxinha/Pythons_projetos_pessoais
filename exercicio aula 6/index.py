valor = float(input("Passe o valor do item "))
quantidade = int(input("Passe a quantidade item comprados "))

valorReal = quantidade * valor

desconto = valorReal * 0.10 

descontoFinal = (valorReal - desconto)



print(f"O valor total vai ser de: R${valorReal}, porém você ganhou um desconto de 10% que ficou por R${descontoFinal: .2f}")