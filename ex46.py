# faça um programa que mostre na tela uma contagem regressiva para o estouro de fogos, indo de 10 até 0, 
# com pausa de 1s entre eles:


from time import sleep

for i in range(10, 0, -1):
    print(i)
    sleep(1)
    # print(f'{" Escolha ":=^40}')
print(f'{" BOOOOMMMMMM ":*^20}')