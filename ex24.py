## crie um programa que leia o nome de uma cidade e diga se ela comaça ou não com o no come "santo"

cdd = str(input("Digite o nome da cidade: "))
rmspace= cdd.strip()
ver_santo= rmspace[0:5].lower== 'santo' # ver se a cidade começa com santo
print(ver_santo)