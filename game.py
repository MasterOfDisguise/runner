__author__ = 'Administrator'
from config import *
from classes import GameScreen

clock = pygame.time.Clock()
game = GameScreen(screen)
pygame.mixer.music.play(-1)
while running:
    screen.fill(black)
    game.draw()
    game.update()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = 0
        if event.type == pygame.KEYDOWN:
            game.runner.key_event(event)
    pygame.display.flip()
    clock.tick(120)
