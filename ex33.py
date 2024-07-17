# faça um prog que leia 3 numeros e mostre qual é o maior e qual é o menor.

x1 = int(input("Insira o primeiro numero: "))
x2 = int(input("Insira o segundo numero: "))
x3 = int(input("Insira o terceiro numero: "))

menor = x1
if x2 < x1 and x2 < x3:
    menor = x2
if x3 < x1 and x3 < x2:
    menor = x3

print("*-"*10)
print(f"Menor é: {menor}")

print("*-"*10)

maior = x1
if x2 > x1 and x2 > x3:
    maior = x2
if x3 > x1 and x3 > x2 :
    maior = x3
print(f"Maior é: {maior} ")
print("*-"*10)     