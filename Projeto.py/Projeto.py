import os #usado para verificar se o arquivo existe
#Criando os arquivos
open("usuarios.txt", "a").close()
open("playlists.txt", "a").close()
open("msc_curtidas.txt", "a").close()
open("msc_descurtidas.txt", "a").close()

 #lista de musicas usando o dicionario para colocar o nome delas e os artistas que cantam
nome_musicas = [
    {"nome": "Shape of You", "artista": "Ed Sherran"},
    {"nome": "Die With A Smile", "artista": "Bruno Mars & Lady Gaga"},
    {"nome": "Birds of a Feather", "artista": "Billie Elish"},
    {"nome": "Blinding Lights", "artista": "The Weekend"},
    {"nome": "TNT", "artista": "Travis Scott"}
]

#colocar usúarios em arquivos:
usuarios = []
with open("usuarios.txt", "r") as us:#Abre o arquivo no modo leitura
    for linha in us:#le cada usuario salvo
        partes = linha.strip().split(',')
        if len(partes) == 3:#ver qnts elementos tem na linha
           nome, nick, senha = partes 
           usuarios.append({'nome': nome, 'nick': nick, 'senha': int(senha)})
#Parte 1 cadastro do usu:
def novo_usu():
    while True:
        print('=== Menu principal ===')
        print('1 Para login!')
        print('2 Para cadastrar!')
        cadastro = input('Digite uma das opções por favor:')
        if cadastro == '1':
            usu = input('Digite seu usúario: ')
            senha = int (input('Digite sua senha: '))

            #funçao any serve para verificar se a expressao é True ou seja esta fazendo a verificação
            #para ver se o usuario e a senha estao inseridos na lista 
            #o u é um dicionario que tambem verifica se as expressoes sao true 
            if any(u['nick'] == usu and u['senha'] == senha for u in usuarios):
                print('Login realizado com sucesso!')
                menu(usu)# chama o menu para o usuario logado 
                break
            else:
                print('Usuário ou senha incorretos, tente novamente!')

        elif cadastro == '2':
            nome = input('Digite seu nome: ')
            nick = input('Digite o usuário que deseja utilizar: ')
            if any(u['nick'] == nick for u in usuarios):
                print("Esse usúario já existe, tente outro!")
                continue
        
            
            while True:
                    nova_senha = int(input('Digite uma senha de 4 números inteiros: '))
                    if nova_senha < 1000 or nova_senha > 9999:
                        print("Digite uma senha de 4 digitos por favor!") 
                    else:
                        break
            usuarios.append({'nome': nome, 'nick': nick, 'senha': nova_senha})
            #salvar novo usu  no arquivo
            with open("usuarios.txt", "a") as u:
                u.write(f'{nome},{nick},{nova_senha}\n')

            print('Cadastro efetuado com sucesso!')
            print("Basta selecionar a opção de login!")
            
        else:
            print("Opção inválida, digite 1 ou 2!")

#Menu de navegação:
def menu(nick):
    while True:
        print('='*50)
        print(f'-- Bem vindo {nick} ao Soptfei! --')
        print('='*50)
        print('Fique a vontade para navegar aqui!')
        print('Basta escolher as opções abaixo: ')
        print('1 --> Buscar e escutar músicas.')
        print('2 --> Playlists.')
        print('3 --> Vizualizar histórico.')
        print('4 --> Encerrar.')
        opc = input('Escolha uma dessas opções: ')
        
        if opc == '1':
            music(nick)
        elif opc == '2':
            gerenciar_playlist(nick)
        elif opc == '3':
            historico(nick)
        elif opc == '4':
            break
        else:
            print('Opção inválida, digite algum dos números por favor!')


#parte 2 do projeto(Buscar e cutir musicas)
def music(nick):
    print("="*50)
    print("Pronto para escutar sua música favorita?")
    print("="*50)

    msc_curtidas = []
    msc_descurtidas = []

    while True:#para repetir a pergunta até acerta
        musica = input('Digite o nome da música que você procura: ')
        for music_tocando in nome_musicas:#percorrendo a lista
                if musica.lower() == music_tocando["nome"].lower():#verificando se a musica esta no dicionario
                    print("Música encontrada!")
                    print(f"Tocando {music_tocando['nome']} de {music_tocando['artista']}...")

                    while True:#para repetir a pergunta do sim e não e do 1 e 2 ate acerta
                        curtir = input('Deseja curtir/descurtir essa música ?: ')
                        if curtir == "sim":
                            while True:
                                resposta = input("Digite 1(curtir) ou 2(descurtir):")
                                if resposta == '1':
                                    if music_tocando in msc_curtidas:
                                        ja_curtida = False
                                        for musica in msc_curtidas:
                                            if musica['nome'] == music_tocando['nome'] and musica['artista'] == music_tocando['artista']:
                                                ja_curtida = True
                                                break
                                        if ja_curtida:
                                            print("Música já foi curtida!")
                                    else:
                                       print(f"{music_tocando['nome']} curtida com sucesso!")
                                       msc_curtidas.append(music_tocando)
                                       with open(f"{nick}- msc_curtidas.txt", 'w') as c:
                                           for musica in msc_curtidas:
                                               c.write(f"{musica['nome']} - {musica['artista']}\n")
                                    break
                                       
                                                    
                                elif resposta == '2':
                                    if music_tocando in msc_descurtidas:
                                        ja_descurtida = False
                                        for musica in msc_descurtidas:
                                            if musica['nome'] == music_tocando['nome'] and musica['artista'] == music_tocando['artista']:
                                                ja_descurtida = True
                                                break
                                        if ja_descurtida:
                                            print("Música já descurtida!")
                                    else:
                                       print(f"{music_tocando['nome']} descurtida com sucessso!")
                                       msc_descurtidas.append(music_tocando)
                                       with open(f"{nick}- msc_descurtidas.txt", "w") as d:
                                         for musica2 in msc_descurtidas:
                                            d.write(f"{musica2['nome']} - {musica2['artista']}\n")
                                    break
                                else:
                                    print("Opção inválida digite 1 ou 2.")
                            break

                        elif curtir == "não":
                            print(f"Tocando novamente {music_tocando['nome']} de {music_tocando['artista']}...")
                            break
                        else:
                            print("Resposta inválida, digite sim ou não! ")
                    while True:
                        print('O que deseja fazer agora?')
                        print('1 --> Buscar outra música.')
                        print('2 --> Voltar ao menu.')
                        op = input("Digite 1 ou 2:")
                        if op == "1":
                            break
                        elif op == "2":
                            return
                        else:
                            print('Opção inválida, digite 1 ou 2.')
                    break
        else:              
          print("Música não encontrada, tente novamente!")
          continue
   
            
#Parte 3(Gerenciar playlists)
def gerenciar_playlist(nick):
    playlist = []
    print('='*100)
    print('Aqui você pode criar as playlists com sua cara, adicionando suas músicas favoritas!')
    print('Mas também pode gerenciar uma playlist já criada.')
    print('='*100)
   

    while True:
        print('Escolha o que quer fazer de acordo com as três opções a baixo:')
        print('1 --> Criar playlist.')
        print('2 --> Gerenciar uma playlist que já exista.')
        print('3 --> Voltar ao menu.')
        play = input("Digite a sua escolha (1,2,3):")

        if play == "1":
            nome_ply = input("Digite o nome que deseja colocar para sua playlist:")
            msc = []

            while True:
                nome_msc = input("Digite o nome da música que deseja adicionar ou 'pronto' para parar:")
                if nome_msc == "pronto":
                    break
                if any(nome_msc.lower() == m['nome'].lower() for m in nome_musicas):
                    print(f"{nome_msc} adicionada em {nome_ply}!")
                    msc.append(nome_msc)
                else:
                    print("Música não encontrada, tente novamente.")

            playlist.append({'nome': nome_ply, 'música': msc})

            with open(f'{nick}- playlists.txt', 'a') as p:
                p.write(f"{nome_ply}: {','.join(msc)}\n")
            
            print(f"Playlist {nome_ply} criada com sucesso!")

        elif play == '2':
            if not os.path.exists(f"{nick}- playlists.txt"):
                print("Nenhuma playlist encontrada!")
                continue

            with open(f"{nick}- playlists.txt", 'r') as arq:
                linhas = arq.readlines()

            if not linhas:
                print("Nenhuma playlist encontrada!")
                continue
            for linha in linhas:
                print(linha.strip())
            
            nome_escolhido = input("Digite o nome da playlist que deseja mexer:")
            for linha in linhas:
                if linha.startswith(nome_escolhido + ':'):#encontra o nome da playlist na linha
                    partes = linha.strip().split(':')#remove espaços em branco e deixa o nome da ply separado da musica
                    nome = partes[0]
                    musicas = partes[1].split(",") if len(partes) > 1 else []
                    break
            else:
                print("Playlist não encontrada!")
                continue
            ply_excluida = False

            while True:
                print("Escolha aqui o que deseja fazer: ")
                print("1 --> Excluir esta playlist..")
                print("2 --> Adicionar novas músicas.")
                print("3 --> Remover música.")
                print("4 --> Voltar")
                opcao = input("Digite sua opção:")

                if opcao == '1':
                    arq_play = open(f"{nick}- playlists.txt", 'w')
                    for linha in linhas:
                        if not linha.startswith(nome_ply + ':'):
                            arq_play.write(linha)
                    arq_play.close()
                    print(f"{nome_ply} excluida com sucesso!")
                    ply_excluida = True
                    break

                elif opcao == '2':
                    while True:
                        nova_msc = input("Digite a nova música que deseja adicionar ou 'pronto' para parar:")
                        if nova_msc == 'pronto':
                            break
                        if any(nova_msc.lower() == m['nome'].lower() for m in nome_musicas):
                            print(f"{nova_msc} adicionada com sucesso!")
                            musicas.append(nova_msc)
                        else:
                            print("Música não encontrada, tente de novo.")
                            continue

                elif opcao == '3':
                    remover = input("Digite o nome da música que deseja excluir:")
                    for m in musicas:
                        if m.strip().lower() == remover.lower():
                            musicas.remove(m)
                            print(f"{m} removida com sucesso.")
                            break
                        else:
                            print("Música não encontrada, tente de novo.")
                
                elif opcao == '4':
                    break
                else:
                    print("Opção inválida, digite algum dos números.")
                    continue
            if not ply_excluida:
             with open(f"{nick}- playlists.txt", 'w') as atualizado:
                for linha in linhas:
                    if not linha.startswith(nome_escolhido  + ':'):
                        atualizado.write(linha)
                atualizado.write(f"{nome_escolhido}: {','.join(musicas)}\n")

                print(f"{nome_ply} atualizada com sucesso!")
        
        elif play == '3':
            break

        else:
            print("Opção inválida, digite algum dos números.")

def historico(nick):
    print("="*50)
    print("Visualize seu histórico aqui!")
    print("="*50)
    print("O que deseja?")
    print("1 --> Visuliazr músicas curtidas.")
    print("2 --> Visualizar músicas descurtidas.")
    print("3 --> Voltar")
    while True: 
        hist = input("Digite algum dos números acima: ")
        if hist == '1':
            if os.path.exists(f"{nick}- msc_curtidas.txt"):
                with open(f"{nick}- msc_curtidas.txt", 'r') as arq_curtidas:
                    linhas = arq_curtidas.readlines()
                    if not linhas:
                        print("Nenhuma música curtida.")#usado caso o arquivo exista mas não tenha nenhuma msc dentro
                    else:
                        print("Músicas curtidas:")
                        for linha in linhas:
                            print(linha.strip())
            else:
                print("Nenhuma música curtida.")#usado caso nenhum arquivo exista
            
        elif hist == '2':
            if os.path.exists(f"{nick}- msc_descurtidas.txt"):
                with open(f"{nick}- msc_descurtidas.txt", 'r') as arq_descurtidas:
                    linhas = arq_descurtidas.readlines()
                    if not linhas:
                        print("Nenhuma música descurtida.")
                    else:
                        print("Músicas descurtidas:")
                        for linha in linhas:
                            print(linha.strip())
            else:
                print("Nnenhuma música descurtida.")
        elif hist == '3':
            break
        else:
            print("Opção inválida digite um dos números acima.")
         
novo_usu()


