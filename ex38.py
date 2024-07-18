# Escreva um programa que leia dois numeros inteiros e compara-os, mostrando na tela uma msg
# - o primeiro valor é maior
# - o segundo valor é maior
# - Não existe valor maior os dois são iguais

num1 = int(input('Insira um número inteiro: '))
num2 = int(input('Insira o segundo número inteiro: '))


if num1 > num2:
    print(f" O primeiro {num1} número é maior!")
elif num1 < num2 : 
    print(f" O segundo {num2} número é maior!")
else:
    print(f"Os números {num1} e {num2} são iguais!")