import yt_dlp
import os


class Main:
    def __init__(self):
        self.qualidadeDownload = 1080
        self.formato = "mp4" 
        self.diretorio = "Downloads"
        self.baixarPlaylistEscolha = False
        self.continuar = True
        self.desenhar_menu()

    def verificarDiretorio(self):
        if not os.path.exists(self.diretorio):
            os.mkdir(self.diretorio)

    def limparConsole(self):
        os.system("cls" if os.name == 'nt' else 'clear')
    
    def definirOpcoes(self):
        opts = {'format' : f'bv*[height<={self.qualidadeDownload}] + ba',
                'outtmpl' : os.path.join(self.diretorio, '%(title)s.%(ext)s'),
                'merge_output_format': f'{self.formato}'}
        if self.baixarPlaylistEscolha == False:
            opts['noplaylist'] = "false"

        if self.formato in ['mp3', 'aac']:
            opts['format'] = 'ba'
            opts['postprocessors'] = [{  
                                'key': 'FFmpegExtractAudio',
                                'preferredcodec': f'{self.formato}',
    }]
                   
        return opts

    def selecaoDoMenu(self,):
        opValidas = ['1', '2', '3', '4', '5']
        selecao = ""
        while selecao not in opValidas:
            selecao = input()
            if selecao not in opValidas:
                print("opção inválida!\n")
    
        if selecao == '1':
            self.baixarVideo()
        elif selecao == '2':
            self.baixarPlaylist()
        elif selecao == '3':
            self.menuMudarQualidade()
        elif selecao == '4':
            self.mudarFormato()
        elif selecao == '5':
            self.continuar = False

    def desenhar_menu(self):
        while self.continuar:
            self.limparConsole()
            print(f"Qualidade selecionada: {self.qualidadeDownload}p")
            print(f"Formato de download: {self.formato}\n")
            print("1 - Baixar vídeo")
            print("2 - Baixar playlist")
            print("3 - Selecionar qualidade")
            print("4 - Selecionar Formato")
            print("5 - Sair do programa")
            self.selecaoDoMenu()

    def baixarVideo(self):
        self.baixarPlaylistEscolha = False
        self.limparConsole()
        url = input("Digite a URL do vídeo (digite 'sair' para sair):")
        if url != 'sair':
            self.verificarDiretorio()
            yt_opts = self.definirOpcoes()
            with yt_dlp.YoutubeDL(yt_opts) as ydlp:
                ydlp.download([url])

    def baixarPlaylist(self):
        self.baixarPlaylistEscolha = True
        self.limparConsole()
        url = input("Digite a URL da playlist (digite 'sair' para sair):")
        if url != 'sair':
            self.verificarDiretorio()
            yt_opts = self.definirOpcoes()
            with yt_dlp.YoutubeDL(yt_opts) as ydlp:
                ydlp.download([url])
    
    def menuMudarQualidade(self):
        self.limparConsole()
        print("Selecione a qualidade desejada:")
        print("1 - 360p")
        print("2 - 480p")
        print("3 - 720p")
        print("4 - 1080p")
        self.selecaoDaQualidade()
    
    def selecaoDaQualidade(self):
        selecao = ""
        while selecao not in ['1', '2', '3', '4']:
            selecao = input()
            if selecao not in ['1', '2', '3', '4']:
                print("opção inválida!\n")
    
        if selecao == '1':
            self.qualidadeDownload = 360
        elif selecao == '2':
            self.qualidadeDownload = 480
        elif selecao == '3':
            self.qualidadeDownload = 720
        elif selecao == '4':
            self.qualidadeDownload = 1080

    def mudarFormato(self):
        self.limparConsole()
        while True:
            print("Digite o formato desejado. Por exemplo 'mp4' \n")
            print("mp4 (vídeo + áudio)")
            print("mkv (vídeo + áudio)")
            print("mp3 (áudio)")
            print("aac (áudio)")
            escolha = input().lower()
            if escolha not in ['mp4', 'mkv', 'mp3', 'aac']:
                print("opção não é valída, por favor digite um formato valído.")
                input()
                self.limparConsole()
            else:
                self.formato = escolha
                break



app = Main()