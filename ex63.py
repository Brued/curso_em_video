# escreva  um prog que leia um num n inteiro qlqr e mostre na tela os n primeiros elementos de uma sequencia de fibonacci

n = int(input('Insira o valor de elementos que quer na sequencia de Fibonacci: '))

a = 0
b = 1
cont = 0
print(f" A sequência de Fiboncci  com {n} termos é dada por: ")
while cont <= n:
    c = a + b
    c = a
    a = b 
    b += c
    cont +=1
    print(f" → {b}", end='')

    # a + b = a
    # a = b 
    # b += a + b

################ guanabara
print('-'*30)
print('Sequencia de Fibonacci')
print('-'*30)
termos = int(input('Quantos termos você quer mostrar? '))
t1= 0
t2= 1
print('~'*30)
print(f'{t1} → {t2}', end='')
c=3
while c <= termos:
    t3 = t1 + t2
    print(f' → {t3}', end = '')
    t1 = t2
    t2 = t3
    c += 1
print(' → Fim')