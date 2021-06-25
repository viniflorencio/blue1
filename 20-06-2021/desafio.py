import random

opcoes = ['papel', 'pedra', 'tesoura']
computador = random.randint(0,2)

placarPC = 0
placarJGD = 0

while True:
    qtd = int(input('escolha a quantidade de jogos: '))
    for i in range(qtd):
        print('escolha uma das opçoes: \n [0] papel \n [1] pedra \n [2] tesoura  ')
        jogador = int(input('escolha sua jogada: '))
        if computador ==0:
            if jogador ==0:
                print('o computador escolheu', opcoes[computador])
                print('voce escolheu', opcoes [jogador])
                print('empatou')
            elif jogador ==1:
                print('o computador escolheu', opcoes[computador])
                print('voce escolheu', opcoes [jogador])
                print('voce perdeu')
                placarPC = placarPC +1
            elif jogador ==2:
                print('o computador escolheu', opcoes[computador])
                print('voce escolheu', opcoes [jogador])
                print('voce venceu')
                placarJGD = placarJGD + 1
        
        if computador ==1:
            if jogador ==0:
                print('o computador escolheu', opcoes[computador])
                print('voce escolheu', opcoes [jogador])
                print('voce ganhou')
                placarJGD = placarJGD + 1
            elif jogador ==1:
                print('o computador escolheu', opcoes[computador])
                print('voce escolheu', opcoes [jogador])
                print('empatou')
            elif jogador ==2:
                print('o computador escolheu', opcoes[computador])
                print('voce escolheu', opcoes [jogador])
                print('voce perdeu')
                placarPC = placarPC+1
        if computador ==2:
            if jogador ==0:
                print('o computador escolheu', opcoes[computador])
                print('voce escolheu', opcoes [jogador])
                print('voce perdeu')
                placarPC = placarPC +1
            elif jogador ==1:
                print('o computador escolheu', opcoes[computador])
                print('voce escolheu', opcoes [jogador])
                print('voce venceu')
                placarJGD = placarJGD +1
            elif jogador ==2:
                print('o computador escolheu', opcoes[computador])
                print('voce escolheu', opcoes [jogador])
                print('empatou')
        print(f'computador: {placarPC} \n jogador: {placarJGD}')   
    print(f'o jogo acabou, a partida terminou: \n computador: {placarPC} \n jogador: {placarJGD}') 
    denovo = input('deseja jogar denovo? (sim ou nao): ')
    if denovo == 'nao':
        break


