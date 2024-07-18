# A confederação nacional de natacao precisa de um programa que leia o ano de nascimento de um atleta e mostre sua categoria e de acordo com a idade:
# - ate 9 anos: mirim
# - ate 14: infantil
# - ate 19 anos: junior
# - ate 20 anos: senior
# - acima: master

ano_nasc = int(input("O ano do seu nascimento: "))

ano = 2024 - ano_nasc

if ano <= 9: 
    print("Sua categoria é MIRIM")
elif ano <=14:
    print("Sua categoria é INFANTIL")
elif ano <= 19: 
    print("Sua categoria é JUNIOR") 
elif ano <= 20:
    print("Sua categoria é SENIOR")
else:
    print("Sua categoria é MASTER")
