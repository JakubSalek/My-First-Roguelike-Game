import pygame
from Creatures.Actor import Actor
from GUI import GraphicElement


# Klasa bohatera gry
class Hero(Actor):

    def __init__(self):
        self.name = "Hero of The Game"
        self.description = "Student of University of Marie Curie Skłodowska. Let's trust he passes his exam"
        self.stats.initPlayer()
        self.positionX = 0
        self.positionY = 0
        self.graphic = GraphicElement().initPlayer()

    # Obsługa ruchu gracza
    def playerMovement(self):
        self.inAction = True
        while self.inAction:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    exit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_UP:
                        self.move(0, -1)
                        return self.stats.getMoveCD()
                    if event.key == pygame.K_DOWN:
                        self.move(0, 1)
                        return self.stats.getMoveCD()
                    if event.key == pygame.K_LEFT:
                        self.move(-1, 0)
                        return self.stats.getMoveCD()
                    if event.key == pygame.K_RIGHT:
                        self.move(1, 0)
                        return self.stats.getMoveCD()
