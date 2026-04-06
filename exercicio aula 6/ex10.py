produto = float(input("Quanto custa o produto?"))
metodoDePagamento = int(input("Qual é o código de método de pagamento? de 1 a 4: "))

metodosDePagamento = {
    1: {
        'tipo': 'À vista em cheque ou dinheiro',
        'desconto': (produto * -0.10) + produto 
    },

    2: {
        'tipo': 'À vista no cartão de crédito',
        'desconto': (produto * -0.05) + produto
    },
    3: {
        'tipo': 'no cartão de crédito em 2 vezes',
        'desconto': produto
    },
    4: {
        'tipo': 'À vista no cartão de crédito',
        'desconto': produto * 1.05
    }
}

metodoEscolhido = metodosDePagamento.get(metodoDePagamento)

descobrir = metodoEscolhido.get('desconto')

print(descobrir)