import pygame
from ClassDardo import *
from ClassCorpo import *
from ClassCenario import *
from ClassGravidade import *
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
        
    def run(self):
       
        while self.running:
            self.handle_events()  
            self.update()         
            self.draw()           
            self.clock.tick(60)

            if self.vidas < 1:
                self.running = False
            if (self.dardo.s[0] > 1450) or (self.dardo.s[1] < -300) or \
                (self.dardo.s[1] > 850) or (self.dardo.s[0] < 100):
                    self.vidas -= 1
                    self.dardo = Dardo()
            if self.corpo.desenha1:
                if self.dardo.rect_colisao.colliderect(self.corpo.rect_colisao_corpo1):
                    self.dardo = Dardo()
                    self.corpo.desenha1 = False
                    self.corpo.desenha2 = True
                    self.vidas -= 1

            elif self.corpo.desenha2:
                if self.dardo.rect_colisao.colliderect(self.corpo.rect_colisao_corpo2):
                    self.dardo = Dardo()
                    self.corpo.desenha2 = False
                    self.corpo.desenha3 = True
                    self.vidas -= 1
            elif self.corpo.desenha3:
                if self.dardo.rect_colisao.colliderect(self.corpo.rect_colisao_corpo3):
                    self.running = False

    def handle_events(self):
        for event in pygame.event.get():
            self.event = event
            if event.type == pygame.QUIT:
                self.running = False
            else:
                self.dardo.puxa_dardo(event)

    def update(self):
        self.dardo.atualiza_colisao()
        self.corpo.atuliza_coli()
        self.dardo.puxa_dardo(self.event)
        vet_grav = self.iman.atualiza_aceleracao(self.dardo.s)
        self.dardo.atualiza_vetor(vet_grav)
        self.corpo.gera_pos()

    def draw(self):
        self.cenario.fundo(self.screen)
        self.iman.desenha_corpo(self.screen)
        self.dardo.desenha_dardo(self.screen, self.event)
        self.corpo.desenha_corpo(self.screen)
        pygame.display.update()

    def quit(self):
        pygame.quit()


if __name__ == "__main__":
    game = Game()
    try:
        game.run()
    except Exception as e:
        print(f"Ocorreu um erro: {e}")
    finally:
        game.quit()