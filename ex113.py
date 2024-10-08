# 113: Reescreva a função leiaInt() que fizemos no desafio 104, incluindo agora a possibilidade da digitação de um número de tipo inválido.
# Aproveite e crie também uma função leiaFloat() com a mesma funcionalidade.
def leiaint(msg):
    while True:
        try:
            n = int(input(msg))
        except (ValueError, TypeError):
            print('~~> \033[31mERRO: por favor, digite um numero inteiro válido.\033[m')
            continue
        except (KeyboardInterrupt):
            print('\033[31mUsuário não preferiu digitar o valor.\033[m')
            return 0
        else:
            return n

def leiafloat(msg):
    while True:
        try:
            n =float(input(msg))
        except (ValueError, TypeError):
            print('~~> \033[31mERRO: por favor, digite um numero inteiro válido.\033[m')
            continue
        except (KeyboardInterrupt):
            print('\033[31mUsuário não preferiu digitar o valor.\033[m')
            return 0 
        else:
            return n

num1 = leiaint('Digite um valor inteiro: ')
num2 = leiafloat('Digite um valor real: ')
print(f'O valor inteiro digitado foi {num1} e o real foi {num2}')