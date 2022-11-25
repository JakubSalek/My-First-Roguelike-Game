import pygame
from Creatures.Actor import Actor
from Creatures.ActorType import ActorType


# Klasa bohatera gry
class Hero(Actor):

    def __init__(self):
        self.name = "Hero of The Game"
        self.description = "Student of University of Marie Curie Skłodowska. Let's trust he passes his exam"
        self.stats.initPlayer()
        self.positionX = 5
        self.positionY = 5
        self.actorType = ActorType.PLAYER

    # Obsługa ruchu gracza
    def playerMovement(self):
        self.inAction = True
        action = 100
        while self.inAction:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    exit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_UP:
                        action = self.move(0, -1)
                    if event.key == pygame.K_DOWN:
                        action = self.move(0, 1)
                    if event.key == pygame.K_LEFT:
                        action = self.move(-1, 0)
                    if event.key == pygame.K_RIGHT:
                        action = self.move(1, 0)
        if action == 2:
            actionAndCD = (action, self.stats.getMoveCD())
            return actionAndCD
        if action in [-1, 1]:
            actionAndCD = (action, 0)
            return actionAndCD
