### Exercício 2- Crie um programa, utilizando dicionário, que simule a baixa de estoque 
# das vendas de um supermercado. Não esqueça de fazer as seguintes validações:​

# Produto Indisponível​
# Produto Inválido​
# Quantidade solicitada não disponível ​

# O programa deverá mostrar para o cliente a quantidade de itens comprados e o total.


itens = {'Batata': 10, 'Arroz': 3, 'Queijo': 9, 'Refrigerante': 4, 'Carne': 7, 'Café': 15, 'Leite': 22}

while True:
    pergunta = input('Gostaria de comprar algum item?: ')
    if pergunta == 'nao':
        break
    print('Escolha um item da loja:\n [0] Batata \n [1] Arroz \n [2] Queijo \n [3] Refrigerante \n [4] Carne \n [5] Café \n [6] Leite \n ')
    pergunta2 = input('Digite o item que deseja')
    pergunta3 = input('Digite a quantidade que deseja do item')