dic = {}

nome = input('Digite seu nome: ')
media = float(input('Digite sua media: '.replace (',', '.')))


dic['nome'] = nome
dic['media'] = media

if media >= 7:
    dic['situação'] = 'aprovado'
elif media >=5 and media < 7:
    dic['situação'] = 'recuperação'
else:
    dic['situação'] = 'reprovado'

print(dic)
