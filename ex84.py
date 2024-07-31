# Faça um prog que leia o nome e peso de várias pessoas, guardando tudo em uma lista. No final, mostre:
# A) Quantas pessoas foram cadastradas.
# B)Uma listagem com as pessoas mais pesadas
# C) uma listagem com as pessoas mais leves.
lista = []
nomepeso = []
c = maior = menor = 0

while True:
    nome = str(input('Digite o nome: '))
    peso = float(input('Digite o peso: '))
    c +=1

    nomepeso.append(nome.upper())
    nomepeso.append(peso)
    lista.append(nomepeso[:])
    nomepeso.clear()    

    if c == 1:
        maior = menor = peso
    else:
        if peso > maior:
            maior = peso
        if peso < menor:
            menor = peso

    sn = str(input('Deseja proseguir? [S/N] ')).upper().strip()
    while sn not in 'SN':
        print('Ops. Tente novamente.')
        sn = str(input('Deseja proseguir? [S/N] ')).upper().strip()
    if sn == 'N':
        break
    
print(f' Temos uma lista {lista}')
print('=_'*20)
print(f'A) Foram cadastradas {c} pessoas.') # posso fazer com len(lista)
print(f'B) O maior peso foi de {maior} Kg.. Peso de ', end ='')
for p in lista:
    if p[1]== maior:
        print(f' [{p[0]}]', end = '')

print(f'\nC) O menor peso foi de {menor} kg. Peso de ', end='')
for p in lista:
    if p[1] == menor:
        print(f'[{p[0]}] ', end='')
print()
