#6.	Escreva uma função que, dado um número nota representando a nota de um estudante, converte o valor de nota para um conceito (A, B, C, D, E e F).


def media(num1):
    if num1 >= 9 and num1<=10:
        return 'A'
    elif num1 >= 8:
        return 'B'
    elif num1 >= 7:
        return 'C'
    elif num1 >= 6:
        return 'D'
    elif num1 >= 5:
        return "E"
    elif num1 <= 4:
        return 'F'
    else:
        return 'Valor Inválido'


resp = float(input('digite sua nota: '))

nota = media(resp)

print(nota)