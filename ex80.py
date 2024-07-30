# crie um programa  que o usuario possa digitar 5 valores numericos e cadastre-os em uma lista,
# já na posição correta de inserção(sem usar o sort()). No final mostre a lista ordenada na tela


l= list()
for i in range(0,5):
    n = int(input('Digite um número: '))
    l.append(n)
print(l)
