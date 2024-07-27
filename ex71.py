# crie um prog que simule o funcionamento de um cx eletronico. No inicio, pergunte qual sera o valor a ser sacada (int) e
# quantas edulas de cada valor serão entregues.
# obs: considere que o caixa possui cedulas de 50, 20 e 10 e 1


saque = int(input('Qual valor a ser sacado? R$ '))

cont50 = cont20 = cont10 = cont1 = 0
while True:
    if saque >=50:
        saque -= 50
        cont50 +=1
    else:
        if saque >= 20:
            saque -= 20
            cont20 += 1
        else: 
            if saque >=10:
                saque -= 10
                cont10 += 1
            else:   
                if saque >= 1:
                    saque -= 1
                    cont1 += 1
    if saque == 0:
        break
print(f""">> Total de cédulas de R$ 50,00 → {cont50}
>> Total de cédulas de R$ 20,00 → {cont20}
>> Total de cédulas de R$ 10,00 → {cont10}
>> Total de cédulas de R$ 1,00 → {cont1}

""")