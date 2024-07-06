#Faça um programa que leia um angulo qlqr 
#mostre na tela o valor do seno, cosse e tangente desse angulo
from math import sin, cos, tan
angulo = float(input('Qual valor do algulo? '))
print(f"Para o valor desse ângulo, temos:\n"
      f"O seno: {sin(angulo):.2f}\n"
      f"O cosseno: {cos(angulo):.2f}\n"
      f"A tangente: {tan(angulo):.2f}")
