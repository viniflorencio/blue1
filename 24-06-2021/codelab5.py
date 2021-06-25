##5.	Faça um programa que calcule através de uma função o IMC de uma pessoa que tenha 1,68 e pese 75kg.

def imc(peso,altura):
  total =  peso / (altura * altura)
  return total


resp1 = float(input('digite sua altura em metros ').replace(',','.'))
resp2 = float(input('digite seu peso em kilos '))

final = imc(resp2,resp1)
print('seu imc é de', final)