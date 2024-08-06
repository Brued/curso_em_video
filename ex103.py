# faça um programa que tenha uma função chamada ficha() que receba dois parametros opcionais; O nome de um jogador e
# quantos gols ele marcou.
# o programa deverá ser capaz de mostrar a ficha do jogador, mesmo que algum dado não tenha sido informado corretamente

def ficha(nome = '<desconhecido>', gol=0):
    return print(f'O jogador {nome} fez {gol}.')


# main
print(f'{'*'*3:<2}{'Ficha do jogador':^10}{'*'*3:>2}')
nome = str(input('Nome do jogador:'))
quant_gol = int(input('Quantos gols ele fez? '))

if nome.strip() == '':
    ficha(gol=quant_gol)
else:
    ficha(nome, quant_gol)