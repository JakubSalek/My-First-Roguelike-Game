import pygame
from Entity import Entity, EntityTypes


# Klasa bohatera gry
class Hero(Entity):
    heroTurn = False

    def __init__(self):
        self.setType(EntityTypes.CHARACTER)

    def setHeroTurn(self, heroTurn):
        self.heroTurn = heroTurn

    # Obsługa ruchu gracza
    def player_movement(self):
        self.setHeroTurn(True)
        while self.heroTurn:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    exit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_UP:
                        self.move("UP")
                        self.setHeroTurn(False)
                    if event.key == pygame.K_DOWN:
                        self.move("DOWN")
                        self.setHeroTurn(False)
                    if event.key == pygame.K_LEFT:
                        self.move("LEFT")
                        self.setHeroTurn(False)
                    if event.key == pygame.K_RIGHT:
                        self.move("RIGHT")
                        self.setHeroTurn(False)
