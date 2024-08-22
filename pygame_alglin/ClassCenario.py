import pygame
import numpy as np
import os
class Cenario:
    def __init__(self):
        base_path = os.path.dirname(os.path.abspath(__file__))
        parq_path = os.path.join(base_path, 'pygame_alglin', 'img', 'parqu.png')

        self.background = pygame.image.load(parq_path)
        self.background = pygame.transform.scale(self.background, (1200, 700))

    def fundo(self, window):
        window.blit(self.background, (0, 0))
