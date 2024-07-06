# Faça um programa que leia um numero de 0 a 9999 e mostre na tela os digitos separados
# num = int(input('Digite um numero de 0 a 9999:'))
# n0 = str(num)
# print(f"Unidade:{n0[3]}\n"
#       f"Dezena: {n0[2]}\n"
#       f"Centena:{n0[1]}\n"
#       f"Milhar: {n0[0]}")

# >>> ACIMEA<<< ESSE DA PROBLEMA PQ SE ESCOLHER UM NUM DE ORDEM 3 ELE DA ERRO




num = int(input('Digite um numero de 0 a 9999:'))
n0 = str(num)

u = num // 1 %10
d = num // 10 %10
c = num // 100 %10
m = num // 1000 %10

print(f"Unidade:{u}\n"
      f"Dezena: {d}\n"
      f"Centena:{c}\n"
      f"Milhar: {m}")



