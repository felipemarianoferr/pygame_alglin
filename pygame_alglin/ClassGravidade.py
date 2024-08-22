import pygame
import numpy as np
import os
class Iman:
    def __init__(self):
        base_path = os.path.dirname(os.path.abspath(__file__))
        iman_path = os.path.join(base_path, 'pygame_alglin', 'img', 'iman.png')
        red_path = os.path.join(base_path, 'pygame_alglin', 'img', 'redsprite.png')
        self.centro = np.array([545,430])
        self.raio = 100
        self.sprite = pygame.transform.scale(pygame.image.load(iman_path), (200, 200))
        self.red_sprite = pygame.transform.scale(pygame.image.load(red_path), (2 * self.raio, 2 * self.raio))
        self.angle = 0

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
        rotated_sprite = pygame.transform.rotate(self.red_sprite, self.angle)

        self.angle += 6

        top_left = (self.centro[0] - rotated_sprite.get_width() // 2, 
                    self.centro[1] - rotated_sprite.get_height() // 2)

        window.blit(rotated_sprite, top_left)
