# faça um prog que leia 3 numeros e mostre qual é o maior e qual é o menor.

x1 = int(input("Insira o primeiro numero: "))
x2 = int(input("Insira o segundo numero: "))
x3 = int(input("Insira o terceiro numero: "))

x = x1
if x2 > x:
    x = x2
if x3 > x:
    x = x3

print("*-"*10)
print(f"Maior é: {x}")

print("*-"*10)

x = x1
if x2 > x:
    x = x2
if x3 > x :
    x = x3
print(f"Menor é: {x} ")
print("*-"*10)     