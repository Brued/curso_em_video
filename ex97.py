# faça um programa que tenha uma função chamada escreva(), que receba um texto qlqr como parametro e mostre uma
# mensagem com tamanho adaptavel.
    
def escreva(msg):
    print(f'~'*len(msg))
    print(msg)
    print(f'{'~'*len(msg)}')

escreva(str(input('Digite sua mensagem: ')))