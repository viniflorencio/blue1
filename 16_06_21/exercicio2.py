import random

painel = []
palavras = ['cadeira', 'estojo', 'sorvete', 'caneta', 'perna', 'basquete', 'amarelo', 'elefante', 'pijama', 'quarentena', 'banheiro', 'cachorro', 'moeda', 'fazenda', 'academia', 'churrasco']
chute = input('escolha uma letra: ')
posicao = 0

escolha = random.choice(palavras)
print(escolha)

escolha_Tratada = len(escolha)

painel = list(range(escolha_Tratada))
print(painel)

if chute in escolha:
     
    print(painel)


painel.insert(posicao,chute)