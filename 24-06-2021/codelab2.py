# Faça um programa, com uma função que necessite de um argumento. A função retorna o valor de caractere ‘P’, 
# se seu argumento for positivo, ‘N’, se seu argumento for negativo e ‘0’ se for 0.

def funcao(arg1):
    if arg1 > 0:
        return 'P'
    elif arg1 == 0:
        return 0
    else:
        return 'N'


num1 = int(input('digite um numero '))
resposta = funcao(num1)
print(resposta)
