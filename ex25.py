#Crie um programa que leia o nome de uma pessoa e diga se ela tem SILVA no nome

nome = str(input("Digite seu nome completo: "))
new= nome.lower()
print(new)
new2= new.strip()
print(new2)
# x= new2.count("silva")

print('silva' in new2)
print('=.'*15)
print("Sim, tem silva no nome.")
print('=.'*15)

print('x'*20)
print('Seu nome tem silva? {}'.format( 'silva' in new2))