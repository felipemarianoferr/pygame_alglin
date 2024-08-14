import pygame
import numpy as np

class Corpo():
    def __init__(self):
        self.r_corpo = 80
        self.v_corpo = 1/75
        self.pers = pygame.transform.scale(pygame.image.load("pygame_alglin/img/a.png"),(175,150))
        self.rect = pygame.Rect(np.array([863,167]), (10, 10))
        self.dia = 0

    def pos_corpo(self, dia):
        return (self.r_corpo * np.cos(2*np.pi*dia*self.v_corpo),
                self.r_corpo * np.sin(2*np.pi*dia*self.v_corpo))
    
    def gera_pos(self):

        x, y = self.pos_corpo(self.dia)
        self.rect.topleft = np.array([x+863,y+167])
        if self.dia == 75:
            self.dia = 0
        else:
            self.dia += 1
    
    def desenha_corpo(self, window):
        #self.pers.fill((255,0,255))
        window.blit(self.pers, self.rect)

