import pygame
import numpy as np

class Dardo:
    def __init__(self):
        self.sprite_original = pygame.transform.scale(pygame.image.load("pygame_alglin\img\dardo.png"),(120,40))
        self.sprite = self.sprite_original
        self.s0 = np.array([20,550])
        self.s = self.s0
        self.v = (np.array([0,0]))
        self.gravidade = np.array([0, 0.8])
        self.rect = pygame.Rect(self.s, (10, 10))

    def normaliza(self, vf, forca):
        mod = np.linalg.norm(vf)
        a = forca/mod
        v_norm = a * vf
        return v_norm

    def angulo(self, vetor):
        mod = np.linalg.norm(vetor)
        cos_v = vetor[0] / mod
        arcos = np.arccos(cos_v)
        angulo = np.degrees(arcos)

        if vetor[1] > 0:
            angulo = -angulo

        return angulo

    def atualiza_vetor(self):

        self.v = self.v + self.gravidade
        self.s = self.s + 0.1 * self.v

        self.rect.topleft = self.s  
        
        
        angulo_rotacao = self.angulo(self.v)
        self.sprite = pygame.transform.rotate(self.sprite_original, angulo_rotacao)
        self.rect = self.sprite.get_rect(center=self.rect.center)
    
    def desenha_dardo(self, window):
        
        window.blit(self.sprite, self.s)
