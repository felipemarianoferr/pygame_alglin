import pygame

class Game:
    def __init__(self, width=800, height=600):
        # Inicializa o Pygame e define as dimensões da tela
        pygame.init()
        self.screen = pygame.display.set_mode((width, height))
        pygame.display.set_caption("Meu Jogo em Pygame")
        self.clock = pygame.time.Clock()

        # Variável para controlar o loop principal
        self.running = True

    def run(self):
        # Loop principal do jogo
        while self.running:
            self.handle_events()  # Tratamento de eventos
            self.update()         # Atualização do estado do jogo
            self.draw()           # Desenho na tela
            self.clock.tick(60)   # Controla a taxa de frames por segundo

    def handle_events(self):
        # Trata os eventos (ex: fechamento da janela)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False

    def update(self):
        # Aqui você pode atualizar o estado do jogo
        pass

    def draw(self):
        # Preenche a tela com preto
        self.screen.fill((0, 0, 0))
        # Atualiza a tela
        pygame.display.update()

    def quit(self):
        # Finaliza o Pygame
        pygame.quit()

# Ponto de entrada do programa
if __name__ == "__main__":
    game = Game()
    try:
        game.run()
    except Exception as e:
        print(f"Ocorreu um erro: {e}")
    finally:
        game.quit()
