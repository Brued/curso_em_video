# ex90
# ler o nome e média do aluno

# BRUNO

# nome = input("Nome:")
# media = float(input("Média: "))
# dic = {'nome': nome, 'media': media, 'situação': }



# if media > 7:
#     print(f"{nome} foi Aprovado.")
# else:
#     print(f"{nome} foi Reprovado.")

# guanabara
aluno = dict ()
aluno['nome'] = str(input("Nome: "))
aluno ['media'] = float(input("Media: "))

if aluno['media'] >= 7:
    aluno['situação'] = ['Aprovado']
elif 5<= aluno['media'] < 7:
    aluno['situação']='Recuperação'
else:
    aluno['situação'] = ['Reprovado']
    
# print(aluno) {'nome': 't', 'media': 5.0, 'situação': 'Recuperação'}
print('-=' * 30)
for k, v in aluno.items():
    print (f' - {k} é igual a {v}')