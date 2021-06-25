#3.	 Faça um programa com uma função chamada somaImposto. A função possui dois parâmetros formais: taxaImposto, 
# que é a quantia de imposto sobre vendas expressa em porcentagem e custo,
# que é o custo de um item antes do imposto. A função “altera” o valor de custo para incluir o imposto sobre vendas.



def somaImposto(taxaImposto,custo):
    return custo*(taxaImposto/100+1)

item = int(input('digite o custo do produto '))
imp = int(input('digite a taxa de imposto do produto '))

resposta = somaImposto(imp,item)

print('o custo do produto é de: ', item, 'reais')
print('o imposto pago sera de:', imp, '%')
print('o valor total da compra foi de',resposta, 'reais')

