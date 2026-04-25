import tkinter as tk 

contas = [
    ("kositis", "123"),
    ("Alfredo", "kositis")
]

janela = tk.Tk()
janela.title("Login")
janela.geometry("400x300")

pagina_login = tk.Frame(janela)
pagina_login.pack()

tk.Label(pagina_login, text="Usuario").pack()
entrada_usuario = tk.Entry(pagina_login)
entrada_usuario.pack()

tk.Label(pagina_login, text="Senha").pack()
entrada_senha = tk.Entry(pagina_login)
entrada_senha.pack()

def login():    
    usuario = entrada_usuario.get()
    senha = entrada_senha.get()
    if (usuario, senha) in contas:
        pagina_login.pack_forget()
        pagina_sistema.pack()
    else:
        mensagem_label['text'] = "erro ao tentar logar"

tk.Button(pagina_login, text="Login", command=login).pack()

mensagem_label = tk.Label(pagina_login, text="você logou com sucesso")
mensagem_label.pack()

pagina_sistema = tk.Frame()
tk.Label(pagina_sistema, text="bem vindo ao programa do Paulo").pack()

janela.mainloop()