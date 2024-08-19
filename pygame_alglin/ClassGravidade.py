import pygame
import numpy as np

class Iman:
    def __init__(self):
        self.centro = np.array([545,500])
        self.raio = 100
        self.sprite = pygame.transform.scale(pygame.image.load("pygame_alglin/img/iman.png"), (200, 200))

    def dist(self,s_obj):
        return np.sqrt((self.centro[0] - s_obj[0])**2 + (self.centro[1]-s_obj[1])**2)
    
    def normaliza(self, s_obj):
        vf = self.centro - s_obj
        mod = np.linalg.norm(vf)
        a = 40 / mod if mod != 0 else 0
        v_norm = a * vf
        return v_norm

    def atualiza_aceleracao(self, s_obj):            
        v_norm = self.normaliza(s_obj)
        return (1/self.dist(s_obj)**2)*v_norm*self.raio*10
    
    def desenha_corpo(self, window):
        pygame.draw.circle(window, (0, 0, 255), self.centro, self.raio)
