# Crie um programa que tenha uma função chamada voto() que vai receber como parametro e ano de nacimento de uma pessoa,
# retornando um valor literal indicando se uma pessoa tem voto negado, opcional ou obrigatório nas eleições;




def voto(ano):
    from datetime import date
    atual = date.today().year 
    idade = atual - ano  
    if idade < 16:
        return f'Negado! Com {idade} não vota'
    elif 16 <= idade < 18:
        return f'Opcional. Com {idade} pode escolher se vota.' 
    elif 18 <= idade < 65:
        return f'Com essa {idade} é obrigatório!'
    else:
        return(f' Com essa {idade} é opcional')
    
#main
n = int(input('Digite o ano de nascimento: '))
print(voto(n))