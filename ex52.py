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
