# # fça um progrma em python que abra e reproduza o audio de um arx mp3.
# import pygame

# # Inicializa o pygame
# pygame.init()

# # Inicia a reprodução de música (substitua 'nome_da_musica.mp3' pelo seu arquivo de música)
# pygame.mixer.music.load('nadamais.mp3')

# # Define o volume (opcional)
# pygame.mixer.music.set_volume(0.5)  # Define o volume para 50% (valores variam de 0.0 a 1.0)

# # Começa a reprodução da música
# pygame.mixer.music.play()

# # Mantém o programa rodando até que a música termine
# while pygame.mixer.music.get_busy():
#     pygame.time.Clock().tick(10)  # Ajusta a taxa de atualização (10 ms)

# # Finaliza o pygame ao término da música
# pygame.quit()

# import pygame

# pygame.init()
# pygame.mixer.music.load('nadamais.mp3')
# pygame.mixer.music.play()
# pygame.event.wait()



#chatgpt
import pygame

pygame.init()

print("Inicializando pygame e carregando música...")
pygame.mixer.music.load('nadamais.mp3')

print("Iniciando reprodução da música...")
pygame.mixer.music.play()

# Mantém o programa em execução até que a música termine
print("Aguardando música terminar...")
while pygame.mixer.music.get_busy():
    pygame.time.Clock().tick(10)  # Ajusta a taxa de atualização para 10ms

print("Música terminou.")

# Finaliza o pygame
pygame.quit()
