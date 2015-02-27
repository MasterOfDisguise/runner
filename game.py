__author__ = 'Administrator'
from config import *
from classes import Game

clock = pygame.time.Clock()
game = Game(screen)
pygame.mixer.music.play(-1)
while running:
    screen.fill(black)
    game.draw()
    game.update()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = 0
        if event.type == pygame.KEYDOWN or event.type == pygame.MOUSEBUTTONDOWN:
            game.handle_events(event)
    pygame.display.flip()
    clock.tick(100)
