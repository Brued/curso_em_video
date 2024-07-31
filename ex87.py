# Aprimore o desafio anterior, mostrando no final:
# A) a soma de todos os valores pares digitados.
# B) A soma dos valores da terceira coluna
# C) O maior valor da segunda linha.

matriz = [[], [], []]
s = b = 0
for l in range (0,3):
    for c in range (0, 3):
        matriz[l].append(int(input(f'Digite um valor para [{l},{c}]: ')))
        # matriz[l][c] = int(input(f'Digite um valor para [{l}, {c}]:))

        if matriz[l][c] % 2 == 0:
            s += matriz[l][c]

    b += matriz[l][2]
    

    # if matriz[2][0] > matriz[2][1] and matriz[2][0] > matriz[2][2]:
    #     maior = matriz[2][0]
    # elif matriz[2][1] > matriz[2][0] and matriz[2][1]> matriz[2][2]:
    #     maior = matriz[2][1]
    # else:
    #     maior = matriz[2][2]

print('-'*30)
for l in range(0,3):
    for c in range(0,3):
        print(f'[{matriz[l][c]:^5}]', end='')
    print()
print()
print(f'A) a soma de todos os pares será → {s}')
print(f'B) a soma da coluna 3 será → {b}')
maior = max(matriz[1])
print(f'C) O maior valor da 2ª linha → {maior}')