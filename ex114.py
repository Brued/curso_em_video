# 114: Crie um código em Python que teste se o site pudim está acessível pelo computador usado.
import urllib
import urllib.request

try:
    site = urllib.request.urlopen('https://www.youtube.com/')
except urllib.error.URLError:
    print('O site do yt não está acessível no momento.')
else:
    print('Consegui acessar o site com sucesso.')