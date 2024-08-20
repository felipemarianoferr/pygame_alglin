import pygame
import numpy as np

class Cenario:
    def __init__(self):
        self.background = pygame.image.load("pygame_alglin/img/parqu.png")
        self.background = pygame.transform.scale(self.background, (1200, 700))

    def fundo(self, window):
        window.blit(self.background, (0, 0))
