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
        
    def run(self):
       
        while self.running:
            self.handle_events()  
            self.update()         
            self.draw()           
            self.clock.tick(60) 

    def handle_events(self):
        for event in pygame.event.get():
            self.event = event
            if event.type == pygame.QUIT:
                self.running = False
            else:
                self.dardo.puxa_dardo(event)

    def update(self):
        self.dardo.puxa_dardo(self.event)
        vet_grav = self.iman.atualiza_aceleracao(self.dardo.s)
        self.dardo.atualiza_vetor(vet_grav)
        self.corpo.gera_pos()

    def draw(self):
        self.screen.fill((255, 255, 255))
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