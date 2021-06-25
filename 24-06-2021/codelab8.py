#DESAFIO -  Data com mês por extenso. 
# Construa uma função que receba uma data no formato DD/MM/AAAA e devolva uma string no formato D de mesPorExtenso de AAAA. 
# Opcionalmente, valide a data e retorne NULL caso a data seja inválida. 
# Considere que Fevereiro tem 28 dias e que a cada 4 anos temos ano bisexto, sendo que nesses casos Fevereiro terá 29 dias.


import calendar




def data(num):
    return calendar.month_name[mes]


resp = input('digite sua data de nascimento no formato DD/MM/AAAA ')

dia = int(resp[0:2])
mes = int(resp[3:5])
ano = int(resp[6:])

resp2 = (data(resp))
print('a data do seu nascimento é',dia,'de',resp2, 'de', ano)


