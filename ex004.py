# faça um programa que leia algo dpelo teclado e mostre na tela o seu tipo primitivo
# e todas as informações possiveis sobre ele

x = input('Digite algo: ')
print('O tipo primitivo desse valor é', type(x))
print('_.' * 10)
print('É um numero?', x.isnumeric())
print('_.' * 10)
print('É uma letra?', x.isalpha())
print('_.' * 10)
print('É espaço?', x.isspace())
print('_.' * 10)
print('Esta em letra minuscula?', x.islower())
print('_.' * 10)
print('Esta em letra maiscula?', x.isupper())

