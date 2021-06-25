# Desafio: Faça um programa que ajude um jogador da MEGA SENA a criar
# palpites.O programa vai perguntar quantos jogos serão gerados e vai sortear 6
# números entre 1 e 60 para cada jogo, cadastrando tudo em uma lista composta.
import random
lista=[]
lista2=[]
lista3=[]

jogo = 6
numeros = 0
quantidade_listas = 0

quantidade = int(input('Digite a quantidade de jogos que você deseja:\n'))

while quantidade != quantidade_listas:
    quantidade_listas +=1
    while numeros != jogo:
        numeros += 1
        numero = random.randint(1,60)
        if numero in lista:
            del()
        lista.append(numero)
       

    lista.sort()
    lista2.append(lista)
    
    numeros=0
    lista=[]
print(lista2)
