# Faça um programa que tenha uma função chamada área(), 
# que receba as dimensões de um terreno retangular (largura e comprimento) 
# e mostre a área do terreno:



def area(num1,num2):
    tamanho = num1 * num2
    print('a area do terreno é de ', tamanho, 'metros')


resp = float(input('digite a largura do terreno: '))
resp2 = float(input('digite o comprimento do terreno: '))

area(resp,resp2)

