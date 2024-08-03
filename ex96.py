# faça um programa que tenha uma função chamada area () , que receba dimensoes de um terreno retangular (largura e compimento)
# e mostre a area do terreno.

def area(l, c):
    area = l * c
    print(f'A área desse terreno é de {l}x{c} = {area} m² ')
    
#prog principal
print('------ ÁREA DO TERRENO ------')
lgr = float(input('Largura do terreno: '))
cmp = float(input('Comprimento do terreno: '))
# Resultado
area(lgr, cmp)
