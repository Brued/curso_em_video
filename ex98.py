# faça um prog que tenha uma função chamada contador(), que receba tres parametros: inicio, fim e passo e realize a contagem
# seu programa tem que realizar tres contagens atraves da funcao criada:

# a) de 1 ate 10, de 1 em 1
# b) de 10 ate 0, de 2 em 2
# c) uma contagem personalizada (user digitara inicio fim e passo)

from time import sleep

def contador(i, f, p):
    # Verifica se o passo é zero, que não faria a contagem funcionar
    if p == 0:
        p = 1
    
    # Para contagem crescente
    if i < f:
        if p < 0:
            p = -p  # Torna o passo positivo se a contagem for crescente
        print(f'>>> Contagem de {i} até {f} de {p} em {p} <<<')
        for k in range(i, f + 1, p):
            print(f' {k}', end = '', flush=True)
            sleep(0.3)
    
    # Para contagem decrescente
    else:
        if p > 0:
            p = -p  # Torna o passo negativo se a contagem for decrescente
        print(f'>>> Contagem de {i} até {f} de {-p} em {-p} <<<')
        for k in range(i, f - 1, p):
            print(f' {k}', end = '', flush=True)
            sleep(0.3)
    
    print()  # Pula para a linha seguinte após o loop


# Programa principal
# Parte A
contador(1, 10, 1)
# Parte B 
contador(10, -1, 2)
# Parte C
print('===- Agora é sua vez -===')
contador(int(input('   Valor inicial: ')), int(input('   Valor final: ')), int(input('   Passo: ')))
