# crie um programa que vai ler  varios numeros e colocar em uma lsita.
# Depois disso, crie duas listas extras que vao conter apenas os valores pares e os valores impares digitados respectivamente.
# Ao final mostre o conteudo das 3 listas geradas


lista = []
lpar = []
limpar =[]
while True:
    n = int(input('Insira um número: '))
    lista.append(n)
    sn = str(input('Deseja continuar?[S/N] ')).upper().strip()
    if n % 2 == 0:
        lpar.append(n)
    else:
        limpar.append(n)
    if sn not in 'SN':
        print('Tente novamente.')
        sn = str(input('Deseja continuar?[S/N] '))
    if sn == 'N':
        break
print('='*25)
print(f'Lista é {lista}')
print(f'Lista par → {lpar} ')
print(f'Lista ímpar → {limpar}')
