# Crie um programa onde 4 jogadores joguem um dado e tenham resultados aleatorios. Guarde esses resultados em um dicionário. 
# No final, coloque esse dicionário em ordem sabendo que o vencedor tirou o maior número do dado.
from random import randint 
from time import sleep as sl
from operator import itemgetter
dic = {'Jogador 1': randint(1,6),
       'Jogador 2': randint(1,6),
       'Jogador 3': randint(1,6),
       'Jogador 4': randint(1,6) }

print('-'*30)
for jogador, valor in dic.items():
    print(f'O {jogador} tirou {valor}')
    sl(1)
print('-'*30)
ranking = list()
ranking = sorted(dic.items(), key = itemgetter(1), reverse = True)


print('>>>> Em ordem <<<<')
for j, valor in enumerate(ranking):
    print(f' {j+1} lugar → {valor[0]} com {valor[1]}.')