from random import randint
from random import choice


def loja_Vazia():
    aluguel_loja = 200
    while True:
        print(f'Esta loja esta disponivel para alugar por {aluguel_loja} o dia')
        print('Ações')
        print('1 - alugar')
        print('2 - sair')
        opcao = input('escolha sua ação: ')
        if opcao == '1':
            #if personagem.dinheiro < aluguel_loja:
                print('voce nao tem dinheiro sufisciente para alugar')
        elif opcao == '1':
            pass
            #personagem.aluguel = True
        elif opcao == '2':
            break
        else:
            print('opção inválida')

def mercearia():
    itens = {'flashlight':0,'hook':0, 'knot':0}
    itens_lista = ['flashlight','hook','knot']
    valores = [400,700,600]
    print('Ola, gostaria de comprar algo?')
    print('')
    while True:
        for i in itens:
            print(i)
        opcao = input('digite o nome do item que deseja comprar, ou digite "sair", para deixar a loja: ')
        if opcao == itens_lista[0]:
            pass
            #if personagem.dinheiro < valores[0]:
                #print('Voce nao tem',valores[0], 'para comprar esse item')
        else:
            print('voce adquiriu', itens_lista[0])
            ##inventario['flashlight':1]
        if opcao == itens_lista[1]:
            pass
            #if personagem.dinheiro < valores[1]:
                #print('Voce nao tem',valores[1], 'para comprar esse item')
        else:
             print('voce adquiriu', itens_lista[1])
            ##inventario['hook':1]
        if opcao == itens_lista[2]:
            pass
            #if personagem.dinheiro < valores[2]:
                #print('Voce nao tem',valores[2], 'para comprar esse item')
        else:
            print('voce adquiriu', itens_lista[2])
            ##inventario['knot':1]
        if opcao == 'sair':
            break

def bar():
    #if personagem.sujo = True:
        #print('voce nao pode entrar no bar fedendo desse jeito')

    teor_alcol = 0
    print ('Bem-Vindo ao Bar:')
    print("")
    while True:
        print("Ações:")
        print("1 - Beber")
        print("2 - voltar para a cidade")
        print("")
        opcao = input("Escolha sua ação:")
        if opcao == '1':
            ##personagem.dinheiro -= 30
            bebida = randint(2,10)
            teor_alcol += bebida
            if teor_alcol > 40 and teor_alcol < 90:
                cena1 = randint(1,30)
                if cena1 == 3:
                    print('Um homem totalmente embrigado esbarra em voce')
                    print()
                    print("1 - fazer ele pedir desculpas")
                    print("2 - deixa por isso mesmo, afinal ele esta embriagado")
                    acao = input('Escolha sua Ação: ')
                    if acao == '1':
                        cena2 = randint(1,5)
                        if cena2 == 2:
                            print ('o homem nao quis se desculpar e lhe agrediu, para seu azar ele é ex lutador de MMA, va para o hospital')
                        #hospital = True
                        else:
                            print('o homem pediu desculpas e ainda pagou uma bebida para voce ')

        if teor_alcol > 90:
            pass
            ##fazer condicao para o personagem apagar
        elif opcao == '2':
            break


def hipodromo():
    cavalos = ['Galã','Relâmpago','Sargento','Bandolero','Duquesa','Pé De Pano'] ##lista com nomes do cavalo
    print ('Bem-Vindo a corrida de cavalos:')
    while True:
        print("")
        print("Ações:")
        print("1 - Apostar em uma corrida")
        print("2 - voltar para a cidade")
        opcao = input("Escolha sua ação:")
        if opcao == '1':
            for i in cavalos:  ##printar a lista de opcoes de aposta
                print (i)
            print()
            aposta = input('em qual cavalo deseja apostar? (digite corretamente o nome do cavalo): ')
            aposta_Tratada = aposta.title().strip()
            quantia = int(input('qual quantia deseja apostar?: '))
            vencedor = choice(cavalos) ## escolhe por aleatoriedade do cavalo vencedor
            print('o cavalo vencedor foi', vencedor)
            if aposta_Tratada == vencedor: ## validacao do vencedor
                print ('Parabens, voce ganhou a aposta')
                quantia = quantia * (len(cavalos)-1) 
                ##personagem.dinheiro += quantia
            else:
                print('Voce perdeu a aposta')
                ## personagem.dinheiro -= quantia
        elif opcao == '2':
            break


def restaurante():
    print('Voce entrou no restaurante')
    while True:
        print("Ações:")
        print("1 - Pedir comida")
        print("2 - Vender seu peixe para o restaurante")
        print("3 - Sair do restaurante")
        opcao = input("Escolha sua ação:")
        if opcao == '1':
            # personagem.fome = False
            # personagem.dinheiro -= 80 ### LIGAR COM O CODIGO PRINCIPAL
            pass       
        if opcao == '2':
            opcao = int(input('Quantos peixes quer vender?: '))
            preco = randint (10,30)
            print('Voce vendeu', opcao, 'peixes, pelo valor de', preco,'a unidade')
            opcao = opcao * preco
            cidade()
            #personagem.dinheiro += opcao      
            ### OPCAO TEM QUE LIGAR COM O DINHEIRO DELE1
        elif opcao == '3':
            break


def cidade():
    while True: ### opcoes do que fazer na cidade
        print("")
        print("Voce esta na Cidade")
        print("Ações:")
        print("1 - Restaurante")
        print("2 - Corrida de cavalos")
        print("3 - Bar")
        print("4 - Mercearia")
        print("5 - Loja vazia")
        print("6 voltar para casa")
        opcao = input("Escolha sua ação:")

        if opcao == '1':
            restaurante() ## condicao para ir no restaurante
            
        elif opcao == '2':
            hipodromo() ##condicao para ir na corrida
        
        elif opcao == '3': ## condicao para ir ao bar
            bar()

        elif opcao == '4':
            mercearia()

        elif opcao == '5':
            loja_Vazia()
        
        elif opcao == '6':
            break

cidade()