with open('comando open/abrirexercicio.txt', 'r', encoding='utf-8') as arquivo:
    mensagens = arquivo.readlines()
    for mensagem in mensagens:
      print(mensagem)
    


