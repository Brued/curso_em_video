#  115a: Vamos criar um menu em Python, usando modularização.
# crie um pequeno sistema de modularização que permita cadastrar pesoas pelo seu nome e idade em um arquivo de texto simples.
# o sistema só vai ter 2 opções: cadastraar uma nova pessoa e listar todas as pessoas cadastradas


from lib.interface import *
from time import sleep

while True:
    resposta = menu(['Ver pessoas cadastradas', 'Cadastrar pessoas', 'Sair do programa'])
    if resposta ==1:
        cabeçalho('Opção 1')
    elif resposta ==2:
        cabeçalho('Opção 2')
    elif resposta ==3:
        cabeçalho('Saindo do sistema')
        break
    else:
        print('\033[31mErro! Digite uma opão válida.\033[m')
    sleep(2)