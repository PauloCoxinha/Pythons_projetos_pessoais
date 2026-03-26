from datetime import datetime

hora = datetime.now().hour 

if hora < 12 and hora > 6:
    print("Bom dia flor do dia")
elif hora > 12 and hora < 18:
    print("Boa tarde princesa")
else:
    print("Boa noite cinderela")



ano = int(input("Em que ano você nasceu? "))
idade = 2026 - ano

condicionamento = input("Você tem um bom condicionamento físico? apenas responda com sim ou não. ")
autorizacao_medica = True

if (idade >= 18 and idade < 35) and (condicionamento == "sim" and autorizacao_medica):
    print("Você está apto para competir") 
else: 
    print("Vai pra casa lazarento")

