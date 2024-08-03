# aprimora o desafio 93 para que ele funcione com vários jogadores, incluindo um sistema de visualizacao de detalhes do aproveitamento
# de cada jogador.


jogador = dict()
partidas = list()
jogadores = list()
while True:
    jogador['nome'] = str(input('Nome do Jogador: ')).upper()
    total_partidas = int(input(f'Quantas partidas {jogador["nome"]} jogou? '))

    for c in range(0, total_partidas):
        partidas.append(int(input(f'    Quantos gols na partida {c+1}? ')))
    jogador['gols'] = partidas[:]
    jogador['total'] = sum(partidas)
    
    jogadores.append(jogador.copy())

    while True:
        continuar = str(input('Deseja continuar[S/N]? ')).upper()
        if continuar in 'SN':
            break
        print('   -> Tente novamente.')
    if continuar == 'N':
        break




print('-='*50)
print(jogadores)
print('-='*50)

print('------- Dados dos Jogadores -------')
print('cod ', end = '')
for i in jogador.keys():
    print(f' {i:<14}', end = '')
print()
print('-'*40)
for k, v in enumerate(jogadores):
    print(f'{ k:>3}', end='')
    for d in v.values():
        print(f' {str(d):<15}', end = '')
    print()
print('-'*40)


while True:
    busca =  int(input('Mostrar dados de qual jogador?\n(999para parar)'))
    if busca == 999:
        break
    if busca >= len(jogadores):
        print(f'ERRO! não existe jogador com código {busca} ')
    else:
        print(f'Dados do jogador → {jogadores[busca]["nome"]}')
        for i, g in enumerate(jogadores[busca]['gols']):
            print(f'   No jogo {i+1} fez {g} gols;')
    print('-'*40)
print('Falouws')


# for j in jogadores:
#     for k, v in jogador.items():
#         print(f'- O campo {k} tem o valor {v}')
#     print('-='*30)
#     print(f'O jogador {jogador["nome"]} jogou {len(jogador["gols"])} partidas.')
#     for i, v in enumerate (jogador['gols']):
#         print(f'   => Na partida {i}, fez {v} goals.')
#     print(f'Foi um total de {jogador["total"]} gols.')