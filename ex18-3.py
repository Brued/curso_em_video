#Faça um programa que leia um angulo qlqr 
#mostre na tela o valor do seno, cosse e tangente desse angulo
from math import sin, cos, tan, radians
angulo = float(input('Qual valor do algulo? '))
print(f"Para o valor desse ângulo, temos:\n"
      f"O seno: {sin(radians(angulo)):.2f}\n"
      f"O cosseno: {cos(radians(angulo)):.2f}\n"
      f"A tangente: {tan(radians(angulo)):.2f}")
