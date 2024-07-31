# Crie um progra onde o usuario possa digitar sete valores numéricos e cadastr-os em uma lista única que mantenha 
# separados os valores pares e impares. No final, mostre os valores pares e impares em ordem crescente.

lista = []
nomepeso = []
c = 0
maior = menor = 0

while True:
    nome = input('Digite o nome: ').strip()
    peso = float(input('Digite o peso: '))
    c += 1
    
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
    
    sn = input('Deseja prosseguir? [S/N] ').strip().upper()
    while sn not in 'SN':
        print('Ops. Tente novamente.')
        sn = input('Deseja prosseguir? [S/N] ').strip().upper()
    if sn == 'N':
        break

print(f'Temos uma lista: {lista}')
print('=_'*20)
print(f'A) Foram cadastradas {c} pessoas.')
print(f'B) O maior peso foi de {maior} kg. Peso de ', end='')
for p in lista:
    if p[1] == maior:
        print(f'[{p[0]}] ', end='')

print(f'\nC) O menor peso foi de {menor} kg. Peso de ', end='')
for p in lista:
    if p[1] == menor:
        print(f'[{p[0]}] ', end='')
print()
