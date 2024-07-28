# crei um  programa que tenha uma tupla totalmente preenchida com uma contagem por extenso, de 0 ate 20.
# seu programa devera ler um numero pelo tc (0 a 20) e mostralo por extenso.

extenso = ('zero','um', 'dois', 'três', 'quatro', 'cinco', 'seis', 'sete', 'oito', 'nove', 'dez',
            'onze', 'doze', 'treze', 'quatorze', 'quinze', 'desesseis', 'desesete', 'desoito', 'desenove', 'vinte' )

numero = int(input('Digite um valor de 0 a 20: '))

print(f'você digitou o número  {extenso[numero]}')