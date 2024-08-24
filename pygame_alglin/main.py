import pygame
from pygame_alglin.ClassDardo import *
from pygame_alglin.ClassCorpo import *
from pygame_alglin.ClassCenario import *
from pygame_alglin.ClassGravidade import *
from pygame_alglin.ClassTelas import *
class Game:
    def __init__(self, width=1200, height=700):

        pygame.init()
        self.screen = pygame.display.set_mode((width, height))
        pygame.display.set_caption("Meu Jogo em Pygame")
        self.clock = pygame.time.Clock()
        self.running = True
        self.dardo = Dardo()
        self.vf = np.array([10,-15])
        self.forca = 90
        self.dardo.v = self.dardo.normaliza(self.vf,self.forca)
        self.corpo = Corpo()
        self.cenario = Cenario()
        self.event = None
        self.iman = Iman()
        self.vidas = 5
        self.fase = 1
        self.menu = True
        self.telas = Telas()
        
    def run(self):
       
        while self.running:
            self.handle_events()  
            self.update()         
            self.draw()           
            self.clock.tick(60)

            if self.vidas < 1:
                self.telas.game_over = True
            if (self.dardo.s[0] > 1450) or (self.dardo.s[1] < -300) or \
                (self.dardo.s[1] > 850) or (self.dardo.s[0] < 100):
                    self.vidas -= 1
                    self.dardo = Dardo()
            if self.fase == 2 and self.dardo.rect_colisao.colliderect(self.dardo.rect_parede):
                self.vidas -= 1
                self.dardo = Dardo()

            if self.corpo.desenha1:
                if self.dardo.rect_colisao.colliderect(self.corpo.rect_colisao_corpo1):
                    self.dardo = Dardo()
                    self.corpo.desenha1 = False
                    self.corpo.desenha2 = True
                    #self.vidas -= 1
                    self.fase = 2
            elif self.corpo.desenha2:
                if self.dardo.rect_colisao.colliderect(self.corpo.rect_colisao_corpo2):
                    self.dardo = Dardo()
                    self.corpo.desenha2 = False
                    self.corpo.desenha3 = True
                    #self.vidas -= 1
                    self.fase = 3
            elif self.corpo.desenha3:
                if self.dardo.rect_colisao.colliderect(self.corpo.rect_colisao_corpo3):
                    self.telas.ganhou = True
                    self.vidas = 5

    def handle_events(self):
        for event in pygame.event.get():
            self.event = event
            if event.type == pygame.QUIT:
                self.running = False
            elif self.menu or self.telas.tela_instrucoes or self.telas.game_over or self.telas.ganhou:
                self.telas.checa_clicou(event)
            elif self.dardo.puxando:
                    self.dardo.puxa_dardo(event)

    def update(self):
        if self.telas.clicou_voltar:
            self.telas.tela_instrucoes = False
            self.telas.tela_menu = True
            self.menu = True
            self.telas.clicou_voltar = False
        if self.menu:
            if self.telas.clicou_jogar:
                self.menu = False
            elif self.telas.clicou_instrucoes:
                self.telas.tela_instrucoes = True
                self.telas.tela_menu = False
                self.menu = False
            self.telas.clicou_jogar = False
            self.telas.clicou_instrucoes = False
        else:
            self.dardo.atualiza_colisao()
            self.corpo.atuliza_coli()
            self.dardo.puxa_dardo(self.event)
            if self.fase != 1:
                vet_grav = self.iman.atualiza_aceleracao(self.dardo.s)
            else:
                vet_grav = np.array([0,0])
            self.dardo.atualiza_vetor(vet_grav, self.fase)
            self.corpo.gera_pos()
        if self.telas.game_over or self.telas.ganhou:
            if self.telas.clicou_jogar:
                self.telas.game_over = False
                self.telas.ganhou = False
                self.dardo = Dardo()
                self.corpo = Corpo()
                self.telas = Telas()
                self.vidas = 5
                self.fase = 1
                self.telas.clicou_jogar = False
                self.menu = True

    def draw(self):
        if self.menu:
            self.cenario.fundo(self.screen)
            self.telas.desenha_tela_menu(self.screen)
            pygame.display.update()
        elif self.telas.tela_instrucoes:
            self.cenario.fundo(self.screen)
            self.telas.desenha_tela_instrucoes(self.screen)
            pygame.display.update()
        elif self.telas.game_over:
            self.telas.desenha_tela_game_over(self.screen)
            pygame.display.update()
        elif self.telas.ganhou:
            self.telas.desenha_tela_vitoria(self.screen)
            pygame.display.update()
        else:
            self.cenario.fundo(self.screen)
            if self.fase != 1:
                self.iman.desenha_corpo(self.screen)
            self.dardo.desenha_dardo(self.screen, self.event, self.fase, self.vidas)
            self.corpo.desenha_corpo(self.screen)
            pygame.display.update()

    def quit(self):
        pygame.quit()


def main():
    game = Game()
    try:
        game.run()
    except Exception as e:
        print(f"Ocorreu um erro: {e}")
    finally:
        game.quit()

if __name__ == "__main__":
    main()