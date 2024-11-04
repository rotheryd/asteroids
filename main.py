import pygame
from constants import *
from player import Player

FPS = 60.0

def main() -> None:
    pygame.init()

    clock = pygame.time.Clock()
    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
    dt = 0

    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        screen.fill("black")
        player.draw(screen)
        pygame.display.flip()
        
        dt = clock.tick(FPS) / 1000


if __name__ == "__main__":
    main()