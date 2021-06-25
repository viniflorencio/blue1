#4.	Faça um programa que calcule o salário de um colaborador na empresa XYZ. 
# O salário é pago conforme a quantidade de horas trabalhadas. 
# Quando um funcionário trabalha mais de 40 horas ele recebe um adicional de 1.5 nas horas extras trabalhadas.



def calculo(sal, horas):
    phora = sal/horas
    if horas > 40:
        horas = horas - 40
        horas = horas * 1.5 + 40
        return phora * horas
    else:
        return sal

resp1 = float(input('digite o seu salario '))
resp2 = float(input('digite a quantidade de horas trabahadas '))

resultado = calculo(resp1,resp2)

print('seu salario no mes sera de', resultado, 'reais')

    
