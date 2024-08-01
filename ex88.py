# Faça um programa que ajude um jogador da mega sena a criar palpites. O prog vai perguntar quantos jogos serao gerados
# e vai sortear 6 numeros entre 1 e 60 para cada jogo cadastrando tudo em uma lista composta.

from random import randint
from time import sleep
quant_jogos = int(input("Quantos jogos serão gerados? " ))

jogos = []

for c in range(quant_jogos):
    sextena = []
    while len(sextena) <6 :
        numeros = randint(1, 60)
        if numeros not in sextena:
            sextena.append(numeros)
    jogos.append(sextena)
    print(f'Jogo {c+1} → {sextena}')
    sleep(1)
print()
print(f'>> Essa é a lista de {quant_jogos} jogos {sorted(jogos)}')

