# crie um prog que leia o ano de nascimento de sete pessoas. No final mostre quants pessoas ainda nao atingiram a 
# maioridade (21ans) e quantas ja sao maiores
cont1 =0
cont2 =0
maior = []
menor = []
for i in range (0,7):

    ano = int(input("Digite seu ano de nascimento: "))
    if  1900 < ano < 2024:
        
        if 2024 - ano >= 21:
            maior.append(ano)
            cont1 += 1
        elif 2024 -ano < 21:
            menor.append(ano)
            cont2 += 1
    else:
        print("Você inseriu um ano inválido, por favor tente novamente. ")
    
print(f"Os que atingiram maioridades {maior} e são de menores {menor}")
print(f" {cont1} { cont2}")


########################

from datetime import date
atual = date.today().year

totmaior = 0
totmenor = 0
ano = int( input('Em que ano a {pessoa}ª nasceu?'))
idade = atual - ano
for pessoa in range (1, 8):

    if idade >= 21: 
        totmaior += 1
    else:
        totmenor += 1
print(f"Ao todo tivemos {totmaior} maiores de idade e {totmenor} menores de idade.")
