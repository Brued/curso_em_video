# desenvolva um prog que leia o nome, idade e sexo de 4 pessoas. no final do programas mostre

# a media de idade do grupo
# qual é o nome do homem mais velho
# quantas mulheres tem menos de 20 anos
s = 0
maioridadehomem = 0
nomevelho = ' '
cont = 0
for i in range (1,5):
    print(f"------- {i}ª pessoa")
    nome = str(input('Nome: ')).strip()
    idade= int(input('Idade: '))
    sexo = str(input('Sexo M/F:')).strip().upper()
    s += idade 
    if i == 1 and sexo in'M':  # posso colocar 'Mm' caso nao quera usar upper
        maioridadehomem = idade 
        nomevelho = nome
    if sexo in 'M' and idade > maioridadehomem:
        maioridadehomem = idade
        nomevelho = nome
    if sexo == 'F' and idade < 20:
        cont += 1


print('=.'*15)
print(f" → A média das idade é {s/4}.")
print(f" → O homem mais velho tem {maioridadehomem} anos e se chama {nomevelho}.")
print(f" → {cont} mulheres tem menos que 20 anos.")



