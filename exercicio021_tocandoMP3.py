#Faça um programa em python que abra e reproduza o áudio de um arquivo MP3.

import pygame
pygame.init()
pygame.mixer.music.load("exercicio021_music.mp3")
pygame.mixer.music.play()

# OPÇÃO 1Mantém o código em loop enquanto a música estiver tocando
#while pygame.mixer.music.get_busy():
#    pygame.time.Clock().tick(10)


# OPÇÃO 2: Mantém o programa rodando até você apertar Enter no terminal
input("Pressione Enter para parar a música...")