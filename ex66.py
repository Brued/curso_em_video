# Crie um prog que leia varios numeros inteiros pelo tc. O prog so vai para quando o valor 999, que pe a condição de parada.
# no final mostre quandots numeros foram digitados e qual foi a soma entre eles (desconsiderando o flag)

i = s = 0
while True:
    n = int(input('Digite um número (Digite 999 para parar): '))
    if n == 999:
        break
    i += 1 
    s += n
    med = s /i
print(f'Foram digitados {i} e a média entre eles é { med :.2f}')