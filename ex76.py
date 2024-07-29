# crie um programa que tenha uma tupla unica com nomes de produtos e seus respectivos precos na sequencia.
# No final, mostre uma listagem de precos organizando os dados em forma tabular.

tp = ('Camiseta', 21.99,
      'Óculos', 15.99,
      'Calça', 79.99,
      'Bermuda', 59.99,
      'Tenis', 99.99,
      'Camiseta', 49.99)

print('*'*30)
print('      Tabela de preços:')
print('*'*30)


for i in range (0, len(tp)):
    if i % 2 == 0:
        print(f"{tp[i]:.<30}", end='')
    else:
        print(f'R$ {tp[i]:5.2f}')


