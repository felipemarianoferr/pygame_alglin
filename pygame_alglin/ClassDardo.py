import pygame
import numpy as np
import os
class Dardo:
    def __init__(self):
        base_path = os.path.dirname(os.path.abspath(__file__))
        dardo_path = os.path.join(base_path, 'img', 'dardo.png')
        ima_path = os.path.join(base_path, 'img', 'ima.png')
        madeira_path = os.path.join(base_path, 'img', 'madeira.png')

        self.sprite_original = pygame.transform.scale(pygame.image.load(dardo_path), (150, 200))
        self.sprite = self.sprite_original
        self.vidas = pygame.transform.scale(pygame.image.load(dardo_path), (75, 100))
        self.s0 = np.array([150, 550], dtype=np.float64)
        self.s = self.s0
        self.v = np.array([0, 0], dtype=np.float64)
        self.controle_intensidade = 0.75
        self.gravidade = np.array([0, 0.8], dtype=np.float64)
        self.rect = pygame.Rect(self.s, (40, 40))
        self.puxando = True
        self.arrastando = False
        self.qtd_bolinhas = 50
        self.distancia_final_max = 400
        self.vetor = np.array([0, 0], dtype=np.float64)
        self.iman = pygame.Rect((470,0), (180, 540))
        self.iman_sprite = pygame.transform.scale(pygame.image.load(ima_path), (180,180))
        self.rect_colisao = pygame.Rect(self.s[0], self.s[1], 40, 15)
        self.rect_parede = pygame.Rect(525, 0, 65, 326)
        self.parede = pygame.transform.scale(pygame.image.load(madeira_path), (65, 82))

    def normaliza(self, vf, forca):
        mod = np.linalg.norm(vf)
        a = forca / mod if mod != 0 else 0
        v_norm = a * vf
        return v_norm

    def atualiza_colisao(self):
        self.rect_colisao = pygame.Rect(self.s[0]+30, self.s[1]-15, 30, 30)


    def restringir_posicao(self, pos):
        x, y = pos
        x = max(0, min(150, x))
        y = max(550, min(700, y))
        return np.array([x, y], dtype=np.float64)
    
    def angulo(self, vetor):
        mod = np.linalg.norm(vetor)
        if mod == 0:
            return 0
        cos_v = vetor[0] / mod
        arcos = np.arccos(cos_v)
        angulo = np.degrees(arcos)

        if vetor[1] > 0:
            angulo = -angulo

        return angulo

    def calcular_trajetoria(self, evento):
        pontos = []

        pos_final = self.restringir_posicao(evento.pos)
        vetor = np.array([self.s0[0] - pos_final[0], 
                        self.s0[1] - pos_final[1]], dtype=np.float64)
        self.v = self.normaliza(vetor, np.linalg.norm(vetor)) * self.controle_intensidade

        pos = self.s0.copy()
        vel = self.v.copy()

        for i in range(self.qtd_bolinhas):
            vel += self.gravidade
            pos += 0.1 * vel

            pontos.append(pos.copy())

            if np.linalg.norm(pos - self.s0) > self.distancia_final_max:
                break

        return pontos

    def atualiza_vetor(self,vet_grav, fase):
        if not self.puxando:
            if fase == 1:
                if self.rect_colisao.colliderect(self.iman):
                    self.gravidade = np.array([0, -3])
                else:
                    self.gravidade = np.array([0, 0.8])

            self.v += self.gravidade + vet_grav
            self.s += 0.1 * self.v

            self.rect.topleft = self.s  
            angulo_rotacao = self.angulo(self.v)
            self.sprite = pygame.transform.rotate(self.sprite_original, angulo_rotacao)
            self.rect = self.sprite.get_rect(center=self.rect.center)
    
    def desenha_dardo(self, window, evento, fase, vidas):
        for i in range(vidas):
            dardo_rotacionado = pygame.transform.rotate(self.vidas, 90)
            window.blit(dardo_rotacionado, (40 + 60 * (i-1), 10))
        if fase == 1:
            window.blit(self.iman_sprite, self.iman.topleft)
        elif fase == 2:
            window.blit(self.parede, self.rect_parede.topleft)
            window.blit(self.parede, self.rect_parede.move(0, 82).topleft)
            window.blit(self.parede, self.rect_parede.move(0, 164).topleft)
            window.blit(self.parede, self.rect_parede.move(0, 246).topleft)
        pos_centralizada = self.s - np.array([self.sprite.get_width() / 2, self.sprite.get_height() / 2])
        window.blit(self.sprite, pos_centralizada)
        if self.arrastando:
            bolas_tamanho = 7
            pontos = self.calcular_trajetoria(evento)
            for ponto in pontos:
                pygame.draw.circle(window, (150, 150, 150), ponto.astype(int), bolas_tamanho)
                bolas_tamanho *= 0.95


    def puxa_dardo(self, evento):
        bola_pos = self.s
        bola_raio = 50
        bola_inicial_x = self.s0[0]
        bola_inicial_y = self.s0[1]
        
        if evento.type == pygame.MOUSEBUTTONDOWN:
            if (bola_pos[0] - bola_raio < evento.pos[0] < bola_pos[0] + bola_raio and
                    bola_pos[1] - bola_raio < evento.pos[1] < bola_pos[1] + bola_raio):
                self.arrastando = True
                self.puxando = True
        elif evento.type == pygame.MOUSEBUTTONUP and self.arrastando:
            posicao = self.restringir_posicao(evento.pos)
            self.arrastando = False
            self.puxando = False
            
            self.vetor = np.array([bola_inicial_x - posicao[0], 
                              bola_inicial_y - posicao[1]], dtype=np.float64)
            self.v = self.normaliza(self.vetor, np.linalg.norm(self.vetor)) * self.controle_intensidade