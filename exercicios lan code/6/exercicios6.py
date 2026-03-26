class Canal:
    def __init__(self, nome, descricao, inscritos):
        self.nome = nome
        self.descricao = descricao
        self.inscritos = inscritos
        self.videos = []
        self.data_publicacao:list[Playlist] =  []


    def inscrever(self, quantidade=1):
        self.inscritos += quantidade

    def postar(self, video):
        if video in self.videos:
            print("Esse video ja foi postado")
            return   
        self.videos.append(video)

    def info_playlists(self):
        for playlist in self.playlists:
            print(playlist.nome)
            playlist.info_videos()


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

class Playlist:
    def __init__(self, nome):
        self.nome = nome

        self.videos:list[Video] = []

    def adicionar_video(self, video):
        if video not in self.videos:
            self.videos.append(video)
        else:
            print("Esse video já esta na playlist")

    def remover_video(self, video):
        if video in self.videos:
            self.video.remove(video)
        else:
            print(f"Esse video não está na playlist")

    def info_video(self):
        for video in self.videos:
            video.info()


video_poo = Video('Python objeto', 'aprenda agora')
video_poo.dar_like()

video_discord_python = Video('Discord bots', 'Aprenda a como criar bots para o discord utilizando python!')

video_discord_python.dar_like()

video_discord_python.comentar('Bom video cara')



canal_kositis.postar(video_discord_python)

playlist_programacao = Playlist('programacao')
playlist_programacao.adicionar_video(video_poo)
playlist_discord = Playlist('Chatbots')
playlist_discord.adicionar_video(video_discord_python)

video_minecraft = Video('Jogano Minezin', 'Mine')
video_deltarune = Video('Jogando deltarune', 'Deltarune')
playlist_games = Playlist('Games')
playlist_games.adicionar_video(video_minecraft)
playlist_games.adicionar_video(video_deltarune)

canal_kositis.postar(video_poo)

canal_kositis.postar(video_minecraft)

canal_kositis.postar(video_deltarune)



print(canal_kositis.videos)

print(canal_kositis.info_playlists)
        