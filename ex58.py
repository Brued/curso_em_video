# melhore o jogo do DESAFIO 28 onde o pc vai pensar em um num 0-10. so que agor ao jgdor vai tentar adivinhar ate acertar
# mostrando no final quantos palpites foram necessarios para vencer.

from random import randint
numPC = randint(0,10)


numuser = int(input('Digite um número de 0 a 10: '))
c=0
while numPC != numuser:
    numuser = int(input('Digite um número de 0 a 10: '))
    c += 1

print('_.'*18)
print(f'Número aleatorio Computador : {numPC}')
print(f"Para acertar o você deu {c} palpites.")
print('_.'*18)

acertou = False
palpites = 0
while not acertou: 
    jogador int(input('Qual o seu palpite?'))
    palpites += 1
    if jogador  == computador:
        acertou = True
    else: 
        if jogador < computador:
        print('Mais >>')
    elif jogador > computador:
        print ('Menos << ')
print(f'Acertou com { palpites} tentativas ')