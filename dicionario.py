# dicionario

pessoas = {'Nome': 'Bruno','Sexo': 'M', 'Idade': 29 }
#print(pessoas['Nome'])

# print formatado
# print(f" O {pessoas["Nome"]} tem {pessoas["Idade"]} anos.")

# printando as chaves

# print (pessoas.keys())  # RESULTADO: dict_keys(['Nome', 'Sexo', 'Idade'])

# print(pessoas.values()) # RESULTADO:  dict_values(['Bruno', 'M', 29])

# print (pessoas.items())  # RESULTADO: dict_items([('Nome', 'Bruno'), ('Sexo', 'M'), ('Idade', 29)]) COMPOSIÇÃO <<<<<<

# por laços 

# for k in pessoas.keys():  
#     print(k)
# RESULTADO :

# Nome
# Sexo
# Idade

# for k in pessoas.values():  
#     print(k)

# RESULTADO


# Bruno
# M
# 29

# for k, v in pessoas.items():
#     print(f'{k}={v}')

# Nome=Bruno
# Sexo=M
# Idade=29


# consigo add sem usar o .append[]

# pessoas ['nome'] = ['Tauan']

# CRIANDO UM DICIONARIO DENTRO DE UMA LISTA
# brasil = []
# estado1 = {'uf': 'Rio de Janeiro', 'sigla': 'RJ'}
# estado2 = {'uf': 'São Paulo', 'sigla' :'SP'}
# brasil.append (estado1)
# brasil.append (estado2)

# print(brasil)

# RESULTADO >>> {'uf': 'Rio de Janeiro', 'sigla': 'RJ'}, {'uf': 'São Paulo', 'sigla': 'SP'}]

# Se eu quiser o elemento 0 da lista com elemento  print(brasil[1]['uf'])


estado = dict()
brasil = list()

for c in range( 0, 3):
    estado ['uf'] = str(input('UF:'))
    estado ['sigla'] = str(input('Sigla do Estado:'))
    brasil.append(estado.copy())
    print(brasil)

    # MAIS BONITO

# for e in brasil :
#     print(e)

# Resultado

# {'uf': 'Minas Gerais', 'sigla': 'MG'}
# {'uf': 'Rio de Janeiro', 'sigla': 'RJ'}
# {'uf': 'São Paulo', 'sigla': 'SP'}

# mais bonito

for e in brasil:
    for k, v in e.items():
        print(f'O campo {k} tem valor {v}')
        # for v in e.values():
        #print(v, end = ' ')
        print ()