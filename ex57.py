# # faça um prog que leia o sexo de uma pessoa, mas só aceite valores MF caso esteja errado peça digitação novmanete ate ter um 
# valor correto.
# r = 'S'
# while r == 'S':
#     sexo = str(input('Digite seu sexo [M/F]: ')).upper()
#     r = str(input( "Quer continuar?[S/N] ")).upper()
# print('Fim')

sexo = str(input('Digite seu sexo [M/F]: ')).upper().strip()

while sexo != 'F' and sexo != 'M':
    print('Dado inválido.')
    sexo = str(input('Digite seu sexo [M/F]: ')).upper().strip()

if sexo == 'M':
    print('Sexo Masculino registrado com successo!')
if sexo == 'F':
    print('Sexo  Feminino registrado com sucesso!')