#Faça um programa que leia o comprimento do cateto oposto e do catedo adj de um trinagulo retangulo
#calcule e mostre o comprimento de hipotenusa
from math import hypot
co = float(input('Qual o valor do Cateto Oposto? '))
ca = float(input('Qual o valor do Cateto Adjacente? '))
print(f'Dado esse triangulo de cateto oposto {co} e cateto adjacente {ca}, a hipotenusa é dada por: {hypot(co, ca)} ')

