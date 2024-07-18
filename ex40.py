# crie um prog que leia duas notas de um aluno e calcule sua média, mostrando uma msg no final de acordo com a media atingida
# -media abaixo de 5 REPROVADO
# - MEDIA ENTRE 5 E 6.9 recuperação
# - MEDIA 7.0 OU SUPERIOR APROVADO

n1 = float( input('Digite a primeira nota: '))
n2 = float( input('Digite a segunda nota: '))
media = (n1 + n2)/2

if media < 5 :
    print(f"Com média {media}, você está REPROVADO")
elif  5 < media < 6.9 :
    print(f"Com média {media}, você está de RECUPERAÇÃO")
else:
    print(f"Com média {media}, você está APROVADO! ")
    print("*---------- PARABÉNS ----------*")

    