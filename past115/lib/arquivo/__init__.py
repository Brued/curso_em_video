from lib.interface import *

def arquivoExiste(nome):
    try:
        a = open(nome, 'rt') # rt que faz a leitura do arquivo
        a.close()
    except FileNotFoundError:
        return False
    else:
        return True

def criarArquivo(nome):
    try:
        a = open(nome, 'wt+') # + cria o arquivo
        a.close()
    except:
        print('Houve um Erro na criação do arquivo')
    else:
        print(f'Arquivo {nome} criado com sucesso.')


def lerarquivo(nome):
    try: 
        a = open(nome, 'rt')
    except:
        print('Erro ao ler o arquivo')
    else:
        cabeçalho('Pessoas cadastradas')
        for linha in a:
            dado = linha.split(';')
            dado[1] = dado[1].replace('\n', '')
            print(f'{dado[0].upper():<30}{dado[1]:>3} anos')

    finally:
        a.close()

def cadastrar( arquivo, nome = 'desconhecido', idade=0):
    try:
        a = open(arquivo, 'at')
    except:
        print('Houve um erro na abertura do arquivo.')
    else:
        try:
            a.write(f'{nome};{idade}\n')
        except:
            print('Houve um erro na hora de escrever os dados.')
        else:
            print(f'Novo registro de {nome} adicionado.')
            a.close()