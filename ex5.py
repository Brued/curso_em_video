# faça um programa que leia um numero inteiro e mostre na tela o seu s
#sucessor e eu antecessor.

num = int(input('Digite um numéro: '))
suc = num + 1
ante = num -1
print('_.' * 10)

print(f'Seu sucessor é \033[32m{suc}\033[m e seu antecessor é \033[33m{ante}\033[m.')
