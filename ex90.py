# Faça um prog que leia nome e média de um aluno guardando também a situação em um dicionario. 
# No final, mostre o conteudo da estrutura na tela.
colecao = {}

nome = str(input('Nome: ')).upper().strip()
media = int(input('Média: '))
colecao['Nome'] = nome
colecao['Media'] = media
if media >= 7:
    colecao['situacao']= 'Aprovado'
elif 5 < media < 7:
    colecao['situacao'] = 'Recuperação'
else: 
    colecao['situacao'] = 'Reprovado'

# print(aluno) {'nome': 't', 'media': 5.0, 'situação': 'Recuperação'}
print('-=' * 20)
for k, v in colecao.items():
    print (f' - {k} é igual a {v}')