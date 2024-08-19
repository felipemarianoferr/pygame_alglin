import pygame
import numpy as np

class Dardo:
    def __init__(self):
        self.sprite_original = pygame.transform.scale(pygame.image.load("pygame_alglin/img/dardo.png"), (150, 200))
        self.sprite = self.sprite_original
        self.s0 = np.array([150, 550], dtype=np.float64)
        self.s = self.s0
        self.v = np.array([0, 0], dtype=np.float64)
        self.controle_intensidade = 0.75
        self.gravidade = np.array([0, 0.8], dtype=np.float64)
        self.rect = pygame.Rect(self.s, (10, 10))
        self.puxando = True
        self.arrastando = False
        self.qtd_bolinhas = 50
        self.distancia_final_max = 400
        self.vetor = np.array([0, 0], dtype=np.float64)
        self.iman = pygame.Rect((500,0), (100, 200))

    def normaliza(self, vf, forca):
        mod = np.linalg.norm(vf)
        a = forca / mod if mod != 0 else 0
        v_norm = a * vf
        return v_norm

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

    def atualiza_vetor(self, vet_grav):

        if not self.puxando:
            if self.rect.colliderect(self.iman):
                self.gravidade = np.array([0, -3])
            else:
                self.gravidade = np.array([0, 0.8])

            self.v += self.gravidade + vet_grav
            self.s += 0.1 * self.v

            self.rect.topleft = self.s  
            angulo_rotacao = self.angulo(self.v)
            self.sprite = pygame.transform.rotate(self.sprite_original, angulo_rotacao)
            self.rect = self.sprite.get_rect(center=self.rect.center)
    
    def desenha_dardo(self, window, evento):

        # if self.s[0] == 150 and self.s[1] == 550:
        #     if evento.type == pygame.MOUSEBUTTONDOWN:
        #         vet_mouse = pygame.mouse.get_pos()
        #         vet_mouse = np.array([vet_mouse[0], vet_mouse[1]])

        #         angulo_inicial = self.angulo(vet_mouse)
        #         self.sprite = pygame.transform.rotate(self.sprite_original, angulo_inicial)
        #         self.rect = self.sprite.get_rect(center=self.rect.center)
        #         print("entrou")

        pygame.draw.rect(window, (255,255,0), self.iman)
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
            
            vetor = np.array([bola_inicial_x - posicao[0], 
                              bola_inicial_y - posicao[1]], dtype=np.float64)
            self.v = self.normaliza(vetor, np.linalg.norm(vetor)) * self.controle_intensidade