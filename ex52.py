# faça um prog que leia um num int e diga se ele é ou nao um numero primo

num = int(input("Insira um número inteiro: "))

        

contador = 0

# if num > 1:
for i in range(2, num - 1):
        if num % i == 0:
            contador += 1

if contador == 0:
    print(f"{num} é Primo")
else:
    print(f"{num} não é Primo")


# gustavo
tot =0
for i in range(1, num + 1):
    if num % i ==0:
        print('\033[32m', end=' ')
        tot += 1
    else:
     print('\033[31m ', end= ' ')
    print(f"{i}", end=' ')
print(f"\033[mO númeoro {num} foi divisível {tot} vezes.")
if tot == 2:
    print('E por isso ele é PRIMO')
else:
    print("E por isso não é primo.")