import pygame

def start():
    pygame.init()
    pygame.mixer.music.load("intro/soundtrack.mp3")
    pygame.mixer.music.play()
