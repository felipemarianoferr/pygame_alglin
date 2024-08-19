import pygame
import numpy as np

class Corpo():
    def __init__(self):
        self.r_corpo = 80
        self.v_corpo = 1/75
        self.r_ameba = 100
        self.v_ameba = 1/75
        self.dia_ameba = 0
        self.pers3 = pygame.transform.scale(pygame.image.load("pygame_alglin/img/a.png"),(175,150))
        self.rect3 = pygame.Rect(np.array([900,400]), (10, 10))
        self.desenha3 = False
        self.pers = pygame.transform.scale(pygame.image.load("pygame_alglin/img/a.png"),(175,150))
        self.rect = pygame.Rect(np.array([863,167]), (10, 10))
        self.dia = 0
        self.pers2 = pygame.transform.scale(pygame.image.load("pygame_alglin/img/a.png"),(175,150))
        self.rect2 = pygame.Rect(np.array([900,70]), (10, 10))
        self.desenha1 = True
        self.desenha2 = False
        self.vfdesce = self.rect2.topleft - np.array([0,600])
        self.vfsobe = np.array([0,600]) - self.rect2.topleft
        self.sobe = False
        self.desce = True
        self.gravidade = np.array([0, 0.8], dtype=np.float64)


    def normaliza(self, vf, forca):
        mod = np.linalg.norm(vf)
        a = forca / mod if mod != 0 else 0
        v_norm = a * vf
        return v_norm

    def pos_corpo(self, dia):
        return (self.r_corpo  * np.cos(2*np.pi*dia*self.v_corpo),
                self.r_corpo  * np.sin(2*np.pi*dia*self.v_corpo))

    
    def pos_ameba(self, dia):
        n_pontas = 5
        angulo = 2 * np.pi * dia * self.v_corpo
        raio_estrela = self.r_corpo * (1 + 0.5 * np.cos(n_pontas * angulo))
    
        return (raio_estrela * np.cos(angulo),
                raio_estrela * np.sin(angulo))


    def gera_pos(self):

        if self.desenha1:
            x, y = self.pos_corpo(self.dia)
            self.rect.topleft = np.array([(x)+863,(y)+167])
            if self.dia == 75:
                self.dia = 0
            else:
                self.dia += 1

        elif self.desenha2:
            if self.desce:
                vf = self.rect2.topleft - self.vfdesce
                vnorm = self.normaliza(vf,28)
                vnorm += self.gravidade
                self.rect2.topleft += 0.1 * vnorm
                if self.rect2.topleft[1] > 570:
                    self.desce = False
                    self.sobe = True

            elif self.sobe:
                vf = self.rect2.topleft - self.vfdesce
                vnorm = self.normaliza(vf,28)
                vnorm += self.gravidade
                self.rect2.topleft -= 0.1 * vnorm
                if self.rect2.topleft[1] < -5:
                    self.desce = True
                    self.sobe = False

        elif self.desenha3:
            x, y = self.pos_ameba(self.dia_ameba)
            self.rect3.topleft = np.array([(x)+900,(y)+400])
            if self.dia_ameba == 75:
                self.dia_ameba = 0
            else:
                self.dia_ameba += 1
                

    def desenha_corpo(self, window):
        
        if self.desenha1:
            window.blit(self.pers, self.rect)
            
        elif self.desenha2:
            window.blit(self.pers2, self.rect2)
        
        elif self.desenha3:
            window.blit(self.pers3, self.rect3)