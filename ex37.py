# escreva um prog que leia um numero int qlqr e peça para o usuario escolher ql sera a base da conversa
# 1 para binario 2 para octal 3 para hexadecimal

num = int(input('Digite um numero: '))
print('=.'*20)
print("""Escolha qual base de conversão quer utilizar: \n 
      \033[32m 1 \033[m para \033[32m Binário \033[m 
      \033[32m 2 \033[m para \033[32m Octal \033[m 
      \033[32m 3 \033[m para \033[32m Hexadecimal\033[m """)
print('=.'*20)

base = int(input('Insira 1, 2 ou 3: '))
print('=.'*20)
if base == 1 :
    print(f"O numero {num} na base binária ficará: \033[31m{bin(num)}\033[m")
elif base == 2: 
    print(f"O numero {num} na base octal ficará: \033[31m{oct(num)}\033[m")
else:
    print(f"O numero {num} na base hexadecimal ficará: \033[31m{hex(num)}\033[m")

