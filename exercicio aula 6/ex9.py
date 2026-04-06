local = int(input("digite sua localização pelo seu código de região: "))
nome_cliente = input("Nome do ciente: ")
numPecas = int(input("Digite o número de peças pedido: "))
nome_vendedor = input("Nome do vendedor: ")

custoPeça = 7.00
custoTotal = numPecas * custoPeça
valorTotal = custoTotal * 1.50
comissaoVendedor = valorTotal * 0.065
lucro = valorTotal - custoTotal - comissaoVendedor    

regioes = {
    1: {"regiao": "sul",
        "frete": 1.00,
        'maxFrete': 0.10
    },
    2: { "regiao": "norte",
        "frete": 1.10,      
        'maxFrete': 0.08        
    },
    3: { 'região': "leste",
        'frete': 1.15,
        'maxFrete': 0.07
    },
    4:  {'região': "oeste",
        'frete': 1.20,
        'maxFrete': 0.11
        },   
    5:  {'região':"noroeste",
         'frete': 1.25,
         'maxFrete': 0.15
    },
    6:  {'região':"sudeste",
         'frete': 1.30,
         'maxFrete': 0.12

} , 7:{'região':"centro-oeste",
        'frete': 1.40,
        'maxFrete': 0.18
    },

    8: { 'região': "nordeste",
         'frete': 1.35,
         'maxFrete': 0.15
    }
}

regiao = regioes.get(local)

if numPecas >= 1000:
    max_frete = regiao.get("maxFrete")
    freteReal = numPecas * max_frete
    
else:
    min_frete = regiao.get("frete")
    freteReal = numPecas * min_frete
    


listaBonita = [
    f"Cliente: {nome_cliente}",
    f"Vendedor: {nome_vendedor}",
    f"Região: {regiao.get('região', 'N/A')}",
    f"Peças: {numPecas}",
    f"Custo Total: R$ {custoTotal:.2f}",
    f"Valor Total: R$ {valorTotal:.2f}",
    f"Frete: R$ {freteReal:.2f}",
    f"Comissão: R$ {comissaoVendedor:.2f}",
    f"Lucro: R$ {lucro:.2f}"
]

print("\n Resumo do pedido:")

for item in listaBonita:
    print(f"- {item}")
