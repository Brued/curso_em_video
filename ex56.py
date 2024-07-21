# desenvolva um prog que leia o nome, idade e sexo de 4 pessoas. no final do programas mostre

# a media de idade do grupo
# qual é o nome do homem mais velho
# quantas mulheres tem menos de 20 anos
lista_idade = [ ]
lista_nome = [ ]

for i in range (0,2):
    nome = str(input('Nome: '))
    lista_nome.append(nome)
    idade= int(input('Idade: '))
    lista_idade.append(idade)
    sexo = str(input('Sexo M/F:'))


maior_idade = lista_idade[0]
for idade in lista_idade:
    if idade > maior_idade:
        maior_idade = idade
        print(f" {maior_idade} {lista_nome(idade)}")

print(f" → A soma das idade é {sum(lista_idade)}")




