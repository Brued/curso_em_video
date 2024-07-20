# dev um prog que leia o primeiro termo e a razao de uma PA. No final mostre os 10 primeiros termos dessa progressao.

primeiro_termo = int(input("Qual é o primeiro termo dessa P.A.? "))
razao = int(input("Qual é a razão dessa P.A.? "))
termos = []
novo_termo = primeiro_termo
for i in range(0, 11):
    termos.append(novo_termo)
    novo_termo += razao
    print(novo_termo, end=' ')

print(' ')

print('>.<'*30)
print(f"os 10 primeiros termos são: {termos} ")
# print('-'*15)

####################################

decimo_termo = primeiro + (10-1)*razao

for c in range(primeiro_termo, decimo_termo, razao):
    print(f"{c}", end = ' → ')