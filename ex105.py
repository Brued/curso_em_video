# faça um programa que tenha uma função notas() que pode receber várias notas de alunos e vai retornar um dicionario com 
# as seguintes informações:
# quantidade de notas
# a maior NotA 
# a menor NotA    
# a média da turma 
# a situacao (opcional)
# adicione tbm as docstrings da função

def notas(*notas, situação = False):
    """
    Esta é a docstring da função.
    Descrião:
    ->Essa função faz com que inserindo as notas obterá a situação.
    :notas: aceita uma ou um conjunto de notas.
    :situação: mostra a situação do aluno.
    :retorna: dicionário com informações e a situação. 
    """

    info = dict()
    info['Quantidade de notas'] = len(notas)
    info['maior'] = max(notas)
    info['menor'] = min(notas)
    info['média'] = sum(notas) / len(notas)
    
    if situação:
        if info['média'] > 7:
            info['situação'] = 'Boa'
        elif 5 < info['média'] < 7: 
            info['situação'] = 'Razoável'
        else:
            info['situação'] = 'Ruim'
    return info



#main
r = notas(8, 9, situação=False)
print(r)

help(notas)