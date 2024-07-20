# faça um programa que calcule a soma entre todos os numeros impares que são multiploes de 3 e que se encontram no intervalo de 1 ate 500.

soma = 0
for i in range(1, 501,2):
    if i%3 ==0:
        print(i)
        soma += i     
print(f"A soma dos ímpares no intervalo de 1 a 500 é {soma}.")





