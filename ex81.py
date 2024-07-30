# crie um programa que vai ler varios numeros e colocar em uma lista. 
# Depois disso, mostre:
# A) quantos numeros foram digitados.
# B) a lista de valores, ordenada em forma decrescente
# C) se o valor 5 foi digitado e esta ou nao na lista


l = []
c = 0
while True:
    n = int(input('Insira um número: '))
    l.append(n)
    c += 1
    sn = str(input('Deseja prosseguir?[S/N] ')).upper().strip()
    while sn not in 'SN':
        sn = str(input('Deseja prosseguir?[S/N] ')).upper().strip()
    if sn == 'N':
        break
print(f'Números na lista {l}')
print('-'*30)
print(f'A) Foram digitados {c} números. ')
l.sort(reverse=True)
print(f'B) A lista de valores em ordem decrescente {l}.')

if 5 in l:
    print('C) O valor 5 faz parte da lista!')
else:
    print('C) O valor 5 não faz parte da lista!')
        

