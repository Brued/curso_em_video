# faça um programa que leia a largura de a altura de uma parede em m
#calcule a sua area e a quantidade de tinta necessario para pinta-la sabendo que a cada
#litro de tinta pinta uma area de 2m^2

largura = float(input('Digite a largura da parede (m): '))
altura = float(input('Digite a altura da parede (m): '))
print( '-' * 30)
area = largura * altura
print(f'A area da parede com {largura}m de largura e {altura}m de altura é: >> {area} << ')
print(f' Você precisará de {area/2} L de tinta para pintá-la.' )