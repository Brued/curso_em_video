# faça um progrmaa que leia um ano qualquer e mostra se ele é bissexto

ano = int(input("Insira um ano: "))
if ano%4==0 and ano % 100 !=0 or ano % 400 == 0:
    print(f"Ano{ano} bissexto.")
else: 
    print(f"{ano} não é bissexto.")
