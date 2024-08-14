import pygame
from ClassDardo import *
class Game:
    def __init__(self, width=800, height=700):

        pygame.init()
        self.screen = pygame.display.set_mode((width, height))
        pygame.display.set_caption("Meu Jogo em Pygame")
        self.clock = pygame.time.Clock()
        self.running = True
        self.dardo = Dardo()
        self.vf = np.array([10,-15])
        self.forca = 90
        self.dardo.v = self.dardo.normaliza(self.vf,self.forca)
        
    def run(self):
       
        while self.running:
            self.handle_events()  
            self.update()         
            self.draw()           
            self.clock.tick(60)

    def handle_events(self):
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False

    def update(self):
        self.dardo.atualiza_vetor()
        

    def draw(self):
        self.screen.fill((0, 0, 0))
        self.dardo.desenha_dardo(self.screen)
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
