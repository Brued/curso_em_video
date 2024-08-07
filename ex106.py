# faça um mini-sistema que utilize o interective help do python. O usuario vai digitar o comando e o manual  vai aparecer.
# Quando o usuario digitar a palavra 'fim' o programa se encerrará.

# Obs. Use cores.
c = ['\033[m ',
     '\033[0;30;41m',
     '\033[0;30;42m',
     '\033[0;30;43m',
     '\033[0;30;44m',
     '\033[0;30;45m',
     '\033[7;30m'
     ]

def helppython(cmd):
    titulo(f"Acessando o manual do comando '{cmd}'", 4)
    print(c[6], end ='')
    help(cmd)
    print(c[0], end ='')


def titulo(msg, cor=0):
    tam = len(msg) + 4
    print(c[cor], end ='')
    print('-'* tam)
    print(f'  {msg}')
    print('-'*tam)
    print(c[0], end ='')



#main
comando = ''
while True:
    titulo('Sistema de ajuda helppython', 2)
    print(c[0], end= '')
    comando = str(input('Função ou biblioteca > '))
    if comando.upper() == 'FIM':
        break
    else:
        helppython(comando)
titulo('Finalizando....Fim.', 1)
