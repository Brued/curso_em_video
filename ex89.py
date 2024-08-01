# Crie um programa que leia nome e duas notas de vários alunos e guarde tudo em uma lista composta. No final, 
# mostre um boletim contendo a media de cada um e permita que o usuario possa mostrar as notas de cada aluno individualmente.

info = []

while True:
    aluno = []
    aluno.append(str(input('Digite o nome do aluno: ')).upper())
    aluno.append(float(input('Digite a primeira nota: ')))
    aluno.append(float(input('Digite a segunda nota: ')))
    escolha = str(input('Deseja continuar? [S/N] ')).upper().strip()
    info.append(aluno)
    if escolha not in 'SN':
        print('Tente novamente.')
        escolha = str(input('Deseja continuar? [S/N] ')).upper().strip()
    if escolha == 'N':
        break
print(f'{"Nº":<4}{"Nome":<10}{"Média}":>8}')
print('-'*30)
for p, nome in enumerate(info):
    print(f'{p:<4}    {info[p][0]:<10}    {(info[p][1] + info[p][2])/2:>8.1f}')
print('-'*30)

while True:
    n = int(input('>> Que aluno quer ver as notas (Obs.: 999 para parar)?  '))
    if n < len(info) :
        print(f'As notas de {info[n][0]} são {info[n][1]} e {info[n][2]}')
    if n == 999:
        print('FINALIZANDO...')
        print('VOLTE SEMPRE!')
        break

# ############
# ficha = []
# while True:
#     nome = str(input('Nome: '))
#     n1 = float(input('Nota 1: '))
#     n2 = float(input('Nota 2: '))
#     media = (n1 + n2) / 2
#     ficha.append([nome, [n1, n2], media])
#     resp = str(input('Quer continuar [S/N] ?'))
#     if resp in 'Nn':
#         break
# print('-='*20)
# print(f'{"No.":<4}{"NOME":<10}{"MÉDIA":>8}')
# print('-'*35)
# for i, a in enumerate(ficha):
#     print(f'{i:<4}{a[0]:<10}{a[2]:>8.1f}')

# while True: 
#     print('-'*35)
#     opc = int(input('Mostrar nota de qual? (999 p/ parar) '))
#     if opc == 999:
#         break
#     if 0 <= opc < len(ficha):
#         print(f'Notas de {ficha[opc][0]} são {ficha[opc][1]}')
#     else:
#         print('Aluno não encontrado. Tente novamente.')

# print('Volte sempre!')