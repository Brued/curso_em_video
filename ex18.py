#Faça um programa que leia um angulo qlqr 
#mostre na tela o valor do seno, cosse e tangente desse angulo
from math import sin, cos, tan
angulo = float(input('Qual valor do algulo? '))
print(f"Para o valor desse angulo, temos: \n O seno: {sin(angulo):.2f} \n O cosseno: {cos(angulo):.2f} \n A tangente:  {tan(angulo):.2f} ")
