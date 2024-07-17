#escreva um programa que faça o computador pensar em um numero inteiro entre 0 e 5 e peça para o usuario tentar
#descrobrir qual fooi o numero escolhido pelo computador
# o prog devera escrever na tela se o usuario venceu ou perdei


from random import choice

num = [1,2,3,4,5]
x = choice(num)

usuario= int(input("Digite um numero de 1 a 5 e tente adivinhar computador escolheu: "))

if usuario == x :
    print("Você venceu!")
else:
    print("Você perdeu!")
# from random import randint
pc = randit(0,5)
