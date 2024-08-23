import pygame
import os

class Telas:
    def __init__(self, width=1200, height=700):
        base_path = os.path.dirname(os.path.abspath(__file__))
        parq_path = os.path.join(base_path, 'img', 'parque.png')
        self.background = pygame.image.load(parq_path)
        self.background = pygame.transform.scale(self.background, (1200, 700))
        self.clicou_jogar = False
        self.clicou_instrucoes = False
        self.clicou_voltar = False
        self.game_over = False
        self.ganhou = False
        self.fonte = pygame.font.Font(None, 50)
        self.fonte_grande = pygame.font.Font(None, 100)
        self.botao_jogar = pygame.Rect((width // 2 - 100), (height // 2 - 150), 200, 100)
        self.botao_jogar_novamente = pygame.Rect((width // 2 - 150), (height // 2 + 100), 300, 100)
        self.botao_jogar_novamente2 = pygame.Rect((width // 2 - 150), (height // 2 + 100), 300, 100)
        self.botao_instrucoes = pygame.Rect((width // 2 - 100), (height // 2), 200, 100)
        self.botao_voltar = pygame.Rect((width - 200), 0, 200, 100)
        self.tela_instrucoes = False
        self.tela_menu = True

    def desenha_tela_menu(self, window):
        pygame.draw.rect(window, (0, 0, 255), self.botao_jogar)
        pygame.draw.rect(window, (0, 0, 255), self.botao_instrucoes)
        jogar = self.fonte.render("Jogar", True, (255, 255, 255))
        instrucoes = self.fonte.render("Instruções", True, (255, 255, 255))
        window.blit(jogar, (self.botao_jogar.x + (self.botao_jogar.width - jogar.get_width()) // 2, 
                            self.botao_jogar.y + (self.botao_jogar.height - jogar.get_height()) // 2))
        window.blit(instrucoes, (self.botao_instrucoes.x + (self.botao_instrucoes.width - instrucoes.get_width()) // 2, 
                                 self.botao_instrucoes.y + (self.botao_instrucoes.height - instrucoes.get_height()) // 2))

    def checa_clicou(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN:
            if self.botao_jogar.collidepoint(event.pos):
                self.clicou_jogar = True
            if self.botao_instrucoes.collidepoint(event.pos):
                self.clicou_instrucoes = True
                self.tela_menu = False
            if self.botao_voltar.collidepoint(event.pos):
                self.clicou_voltar = True
                self.tela_instrucoes = False
                self.tela_menu = True
            if self.botao_jogar_novamente.collidepoint(event.pos) and self.game_over:
                self.clicou_jogar = True
                self.tela_menu = True
            if self.botao_jogar_novamente2.collidepoint(event.pos) and self.ganhou:
                self.clicou_jogar = True
                self.tela_menu = True

    def desenha_tela_vitoria(self, window):
        window.blit(self.background, (0, 0))
        vitoria_texto = "PARABÉNS! VOCÊ VENCEU!"
        mensagem_jogar_novamente = "DESEJA JOGAR NOVAMENTE?"

        vitoria_renderizada = self.fonte_grande.render(vitoria_texto, True, (0, 0, 0))
        jogar_novamente_renderizada = self.fonte.render(mensagem_jogar_novamente, True, (0, 0, 0))

        window.blit(vitoria_renderizada, ((1200 - vitoria_renderizada.get_width()) // 2, 100))
        window.blit(jogar_novamente_renderizada, ((1200 - jogar_novamente_renderizada.get_width()) // 2, 300))

        pygame.draw.rect(window, (0, 0, 255), self.botao_jogar_novamente2)
        jogar = self.fonte.render("Jogar Novamente", True, (255, 255, 255))
        window.blit(jogar, (self.botao_jogar_novamente2.x + (self.botao_jogar_novamente2.width - jogar.get_width()) // 2, 
                            self.botao_jogar_novamente2.y + (self.botao_jogar_novamente2.height - jogar.get_height()) // 2))

    def desenha_tela_instrucoes(self, window):
        instrucoes_texto = [
            "Instruções do Jogo de Lançamento de Dardo",
            "",
            "Objetivo do Jogo:",
            "O objetivo do jogo é lançar o dardo com precisão e força",
            "suficientes para acertar o alvo",
            "",
            "Como Jogar:",
            "1. Clique e segure o botão esquerdo do mouse para puxar o dardo.",
            "2. Arraste o mouse para trás para ajustar a força e o ângulo.",
            "3. Solte o botão do mouse para lançar o dardo em direção ao alvo.",
            "",
            "Dicas:",
            "- Evite obstáculos que possam desviar o dardo.",
        ]

        for i, linha in enumerate(instrucoes_texto):
            linha_renderizada = self.fonte.render(linha, True, (0, 0, 0))
            window.blit(linha_renderizada, (50, 50 + i * 40))

        pygame.draw.rect(window, (0, 0, 255), self.botao_voltar)
        voltar = self.fonte.render("Voltar", True, (255, 255, 255))
        window.blit(voltar, (self.botao_voltar.x + (self.botao_voltar.width - voltar.get_width()) // 2, 
                             self.botao_voltar.y + (self.botao_voltar.height - voltar.get_height()) // 2))

    def desenha_tela_game_over(self, window):
        window.blit(self.background, (0, 0))
        game_over_texto = "GAME OVER!"
        mensagem_perdeu = "VOCÊ PERDEU!"
        mensagem_jogar_novamente = "DESEJA JOGAR NOVAMENTE?"

        game_over_renderizada = self.fonte_grande.render(game_over_texto, True, (255, 0, 0))
        perdeu_renderizada = self.fonte.render(mensagem_perdeu, True, (255, 0, 0))
        jogar_novamente_renderizada = self.fonte.render(mensagem_jogar_novamente, True, (0, 0, 0))

        window.blit(game_over_renderizada, ((1200 - game_over_renderizada.get_width()) // 2, 50))
        window.blit(perdeu_renderizada, ((1200 - perdeu_renderizada.get_width()) // 2, 200))
        window.blit(jogar_novamente_renderizada, ((1200 - jogar_novamente_renderizada.get_width()) // 2, 300))

        pygame.draw.rect(window, (0, 0, 255), self.botao_jogar_novamente)
        jogar = self.fonte.render("Jogar Novamente", True, (255, 255, 255))
        window.blit(jogar, (self.botao_jogar_novamente.x + (self.botao_jogar_novamente.width - jogar.get_width()) // 2, 
                            self.botao_jogar_novamente.y + (self.botao_jogar_novamente.height - jogar.get_height()) // 2))
