import pygame
from Actor import Actor
from GUI import GraphicElement


# Klasa bohatera gry
class Hero(Actor):
    heroTurn = False

    def __init__(self):
        self.name = "Hero of the Game"
        self.description = "Student of University of Marie Curie Skłodowska"
        self.actorStats.initPlayer()
        self.positionX = 15
        self.positionY = 8
        self.graphic = GraphicElement().initPlayer(self.positionX, self.positionY)

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
                        if self.move("UP"):
                            self.setHeroTurn(False)
                    if event.key == pygame.K_DOWN:
                        if self.move("DOWN"):
                            self.setHeroTurn(False)
                    if event.key == pygame.K_LEFT:
                        if self.move("LEFT"):
                            self.setHeroTurn(False)
                    if event.key == pygame.K_RIGHT:
                        if self.move("RIGHT"):
                            self.setHeroTurn(False)
