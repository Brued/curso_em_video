# frase = 'Eu tenho um coelho.'
# # print(frase[::2])
# print(frase.count('e'))
# print(len(frase))

# Crie um programa que leia o nome completo de uma pessoa e mostre:
# o nome com todas as letras maisculas
# o nome com todas minusculas
# quantas letras ao todo sem (sem considerar espaços)
# quantas letras tem o primeiro nombre


nome = str(input('Insira seu nome completo:'))
print('-_' *20)
nome_splitado= nome.split()
quant = len(nome) - nome.count(' ')
print(f"Nome com todas Maiúsculas: {nome.upper()} \n"
      f"Nome com todas Minúsculas: {nome.lower()}\n"
      f"O seu nome tem {quant} letras.\n" 
      f"O seu primeiro nome tem {len(nome_splitado[0])} letras.") # sem usar o split >> usar o nome.find(' ')
print('-_' *20)


# Aula >>> remover os espaços .strip()

