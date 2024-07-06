# faça um algoritmo que leia o precco de um produto e mostre o eseu novo preco
#com 5% de desconto.

preco = float(input('Digite o preço do produto: '))
novo_preco = preco - preco * (5/100)
print('-' *30)
print(f'O preço R$ {preco} com desconto de 5% é : R${novo_preco}.')
