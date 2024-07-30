# crie um programa  que o usuario possa digitar 5 valores numericos e cadastre-os em uma lista,
# já na posição correta de inserção(sem usar o sort()). No final mostre a lista ordenada na tela


l= list()
for i in range(0,5):
    n = int(input('Digite um número: '))
    l.append(n)

    # if i == 0: # se o numero for o primeiro somente adiciono
    #     l.append(n)
    # elif n > lista[-1]: # se o numero n for maior que o ultimo numero
    #     l.append(n)
    # # os comando acima sao iguais entao:
    if i == 0 or n > lista[-1]:
        l.append(n)
    else:
        pos = 0
        while pos < len(l):
            if n <= l[pos]:
                lista.insert(pos, n)
                break
            pos += 1
    
print(f'Os valores digitados em ordem foram {l}')






############user
lista = list()
for c in range(5):
    n = int(input('Digite um número: '))
    if c == 0 or n > max(lista):  # Initial number
        lista.append(n)
    else:
        for i, v in enumerate(lista):  # Analisando cada número da lista
            if n < v:  # Se o número atual for maior do que foi digitado
                lista.insert(i, n)  # Insere na frente dele na lista
                break  # Feito isso, não precisamos continuar nesse loop
    print(f'{n} inserido na posição {lista.index(n)}')
print('--' * 22, f'\nValores digitados em ordem: {lista}')