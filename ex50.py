# Desenvolva um prog que leia seis numeros inteiros e mostre a soma apenas daqueles que forem pars.
# se o valor digitado for impar desconsidere-o
soma = 0
for i in range (1,7):
    num = int(input(f"Insira um número: "))
    if num % 2 == 0:
        soma += num
print('-*'*18)
print(f"A soma dos números pares  será: {soma}")
print('-*'*18)
