class Canal:
    def __init__(self, nome, descricao, inscritos):
        self.nome = nome
        self.descricao = descricao
        self.inscritos = inscritos
        self.videos = []


    def inscrever(self, quantidade=1):
        self.inscritos += quantidade

    def postar(self, video):
        if video in self.videos:
            print("Esse video ja foi postado")
            return   
        self.videos.append(video)


class CanalEmpresarial(Canal):
    def __init__(self, nome, descricao, inscritos):
        super().__init__(nome, descricao, inscritos)
        self._equipe = []
    
    @property
    def equipe(self):
        return self._equipe
    
    def adicionar_membro(self, membro):
        if membro not in self._equipe:
            self._equipe.append(membro)  
        else:
            print('Esse membro já esta na equipe')

    def remover_membro(self, membro):
        if membro in self._equipe:
            self._equipe.remove(membro)
        else: 
            print("O membro não está na equipe")
    
canal_kositis = Canal('Kositis', 'Amo minha vida', 9000)
canal_lancode = Canal('lancode', 'gatos', 1500)
canal_einstein = Canal('einstein', 'ciencia', 9000000)
canal_guanabara = Canal('guanabara', 'paixão por ensinar', 2500000)
canal_profissional = CanalEmpresarial('caio', 'programadores de plantao', 2000) 

class Video:
    def __init__(self, nome, descricao):
        self.nome = nome
        self.descricao = descricao

        self.visualizacoes = 0
        self.likes = 0
        self.deslikes = 0
        self.comentarios = []

    def __repr__(self):
        return f"<{self.nome}>"

    def assistir(self):
        self.visualizacoes += 1

    def dar_like(self):
        self.likes += 1

    def dar_deslike(self):
        self.deslikes += 1
    

    def comentar(self, comentario):
        self.comentarios.append(comentario)

    def mostrar(self):
        print(self.nome)
        print(self.descricao)
        print(self.visualizacoes)
        print(self.likes)
        print(self.deslikes)
        print(self.comentarios.__len__)

video_poo = Video('Python objeto', 'aprenda agora')
video_poo.dar_like()

video_discord_python = Video('Discord bots', 'Aprenda a como criar bots para o discord utilizando python!')

video_discord_python.dar_like()

video_discord_python.comentar('Bom video cara')

canal_kositis.postar(video_discord_python)

canal_kositis.postar(video_poo)

print(canal_kositis.videos)
        