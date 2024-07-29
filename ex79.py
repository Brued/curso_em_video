# crie um prog que o usuario possa digitar varios valores numericos e cadastre-os em uma lista. 
# Caso o numero ja exista la dentro, ele nao sera adicionado. No final, serao exibidos todos os valores únicos digitados,
# em ordem crescente.

lista = list()

while True:
    num = int(input('Digite um número:'))
    if num not in lista:
        lista.append(num)
    opcao = str(input('Deseja continuar? [S/N] ')).upper().strip()
    while opcao not in 'SN':
        print('->> OPS. Digite uma opção válida.')
        opcao = str(input('Deseja continuar? [S/N] ')).upper().strip()
    if opcao == 'N':
        break
lista.sort()
print('*'*50)
print(f'Os números em ordem crescente será: {lista}')
print('*'*50)