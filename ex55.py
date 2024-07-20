# faça um prog que leia o peso de 5 pessoas. No final, mostre qual foi o maior e o menor peso lido.


list = []
for i in range (0, 5):
    peso= float(input(" Qual o valor do seu peso (Kg): "))
    list.append(peso)

print(list)
print(f" O maior peso é {max(list)} e o menor é {min(list)}")

##############################################
menor_elemento = list[0]
maior_elemento = list[0]
for i in range (0, 5):
    peso= float(input(" Qual o valor do seu peso (Kg): "))
    list.append(peso)
    for elemento in list:
        if elemento > maior_elemento:
            maior_elemento = elemento
    for elemento in list:
        if elemento < menor_elemento:
            menor_elemento = elemento
        
print(f" O maior elemento da lista é {maior_elemento} e o menor é {menor_elemento}")
