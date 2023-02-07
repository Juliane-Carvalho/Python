tipo_partida = 0
peças = 0
peca_usuario = 0

def computador_escolhe_jogada(n,m):

    if n <= m:
        return n
    else:
        resto = n%(m+1)
        if resto > 0:
            return resto
        else:
            return m

    #estratégia vencedora comp.

def usuario_escolhe_jogada(n,m): 
    
    peca_usuario = int(input("Quantas peças você vai tirar? "))
    
    while peca_usuario > n or peca_usuario < 1 or peca_usuario > m:
         peca_usuario = int(input("Oops! Jogada inválida! Tente de novo. "))  
    return peca_usuario

def partida():
    vez_do_computador = True
    n = int(input("Quantas peças? ")) #numero de peças
    m = int(input("Limite de peças por jogada? ")) #numero maximo

    if n%(m+1) == 0:
        vez_do_computador = False
        print("\nVocê começa!\n")
    else:
        print("\nComputador começa!\n")
    
    while n > 0:

        if vez_do_computador:
            jogada = computador_escolhe_jogada(n, m)
            vez_do_computador = False
            if jogada == 1:
                print("O computador tirou uma peça.")
            else:
                print("O computador retirou {} peças.".format(jogada))
        else:
            jogada = usuario_escolhe_jogada(n,m)
            vez_do_computador = True
            if jogada == 1:
                print("Você tirou uma peça.")
            else:
                print("Você tirou {} preças.".format(jogada))

        n = n - jogada
        if n == 1:
            print("Agora resta apenas uma peça no tabuleiro.\n")
        elif n > 1:
            print("Agora restam {} peças no tabuleiro.\n".format(n))

    if vez_do_computador:
        print("Fim do jogo! Você ganhou!")
        return 1
    else:
        print("Fim do jogo! O computador ganhou!\n")
        return 0

def campeonato():

    
    usuario = 0
    computador = 0
    n = 1
    for _ in range(3):

        print("**** Rodada", n,"****\n")
        n += 1
        vencedor = partida()
        

        if vencedor == 1:
            usuario += 1
        else:
            computador += 1
   
    print("**** Final do Campeonato! ****\n")
    print("Placar: Você {} X {} Computador".format(usuario, computador))
    
while tipo_partida == 0:

    print("Bem-vindo ao jogo NIM! Escolha: \n")
    print("1 - para jogar uma partida isolada")
    print("2 - para jogar um campeonato 2")

    tipo_partida = int(input(""))

    if tipo_partida == 1:
        print("Voce escolheu uma partida isolada!")
        partida()
        break
    
    elif tipo_partida == 2:
        print("Voce escolheu um campeonato!\n")
        campeonato()
        break
    
    else:
        print("Opção Inválida!")
        tipo_partida = 0

        


