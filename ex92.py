# Crie um prog que leia nome, ano de nascimento e carteira de trabalho e cadastre-os em um dicionário se por acaso a ctps 
# for diferente de zero o dicionario também recebera o ano de contratacao e o salario. 
# Calcule e acrescente alem da idade, com quantos anos a pessoa vai se aposentar.


dados = {}
nome = str(input('Nome:'))
from datetime import datetime
data_e_hora_hoje = datetime.today()
ano_atual = data_e_hora_hoje.year

ano_nascimento = int(input('Ano de Nascimento: '))
ctps = int(input('Carteira de Trabalho (se não tem digite 0): ')) 

dados['Nome'] = nome.upper()
idade = ano_atual - ano_nascimento
dados ['Idade'] = idade
if ctps == 0:
    dados['CTPS'] = ctps
else:
    contrationyear = int(input('Qual o ano de contratação: '))
    salary = int(input('Qual o salário? ')) 
    yearJob = 35 - (ano_atual - contrationyear)

    dados['CTPS'] = ctps
    dados['Contratação'] = contrationyear
    dados['Salário'] = salary
    dados['Aposentadoria'] = idade + yearJob

print(f'{"-"*5}{'Dados Pessoais' :^8}{"-"*5}')
for k, v in dados.items():
    print(f'{k} → {v}')
