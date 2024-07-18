# desenvolva um prog que leia o comprimento de 3 retas e diga ao usuario se ela podem ou nao formar um triangulo.

x = int(input("Insira o comprimento da reta um: "))
y = int(input("Insira o comprimento da reta dois: "))
z = int(input("Insira o comprimento da reta três: "))


#  Condição de existencia
# x + y > z
# z + x > y
# y + z > x

if x + y > z and z + x > y and y + z > x :
    print(f"Os valores {x}, {y} e {z} formam um triangulo.")
else: 
    print(f"Os valores \033[4;31m{ x} , {y} e {z} não formam um triangulo.")

    