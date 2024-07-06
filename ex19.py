# um professor quer sortear um dos seus quatro alnos para apagar o quadro.
# faça um programa que ajude ele, levando o nome deles e escrevendo o nome escolhido.

from random import choice
aluno1= input('Nome do primeiro aluno: ')
aluno2= input('Nome do segundo aluno: ')
aluno3= input('Nome do terceiro aluno: ')
aluno4= input('Nome do quarto  aluno: ')
nomes =  [aluno1, aluno2, aluno3, aluno4]
print('_+' *15)
print(f' O aluno {choice(nomes)} irá apagar o quadro.')
print('_+' *15)