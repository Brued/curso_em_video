# faça um programa que tenha uma função chamada escreva(), que receba um texto qlqr como parametro e mostre uma
# mensagem com tamanho adaptavel.
    
def escreva(msg):
    tam = len(msg) + 4
    print(f'~'*tam)
    print(f'  {msg}')
    print(f'{'~'*tam}')

#Programa principal
escreva(str(input('Digite sua mensagem: ')))