# crie um prog que leia o nome e o preco de varios produtos. o prog deverá perguntr se o usuario quer continuar e no final mostra
# A qual é o total gasto na compra
# B quantos produtos custam mais de 1000RS
# C qual é o nome do produto mais barato


s = i = 0
barato = None
nome_barato = ''
while True: 
    nome = str(input('Digite o nome do produto: '))
    preco = float(input('Digite o preço do produto: '))
    continuar = ' '
    s += preco
    if barato is None or preco < barato:
        barato = preco
        nome_barato = nome

    while continuar not in 'SN':
        continuar = str(input('\033[33m>>>Deseja continuar?[S/N]\033[m')).strip().upper()
    if continuar == 'N':
        break
    
    if preco > 1000:
        i += 1

    
print('°°° Vamos analisar sua compra °°°')
print(f""">>> Total gasto na compra foi de {s}
>>> {i} produtos custam mais que R$ 1.000,00
>>> o nome do produto mais barata é {nome_barato} com valor de {barato}
""")