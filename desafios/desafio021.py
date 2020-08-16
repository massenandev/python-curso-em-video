import pygame

pygame.init()
# essa musica deve estar no mesmo diretorio do arquivo.py
pygame.mixer.music.load('musica.mp3')
pygame.mixer.music.play()
pygame.event.wait()

