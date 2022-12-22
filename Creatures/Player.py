import pygame
from Creatures.Actor import Actor
from Creatures.ActorStatistics import Statistics
from Creatures.ActorType import ActorType
from Items.Inventory import Inventory
from Map.ActionType import ActionType


# Klasa bohatera gry
class Hero(Actor):

    def __init__(self):
        self.name = "Hero of The Game"
        self.description = "Student of University of Marie Curie Skłodowska. Let's trust he passes his exam"
        self.positionX = 0
        self.positionY = 0
        self.actorType = ActorType.PLAYER
        self.stats = Statistics(self.actorType)
        self.inventory = Inventory()

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
        if action == ActionType.MOVE:
            actionAndCD = (action, self.stats.movementCoolDown)
            return actionAndCD
        if action == ActionType.ATTACK_MONSTER:
            actionAndCD = (action, self.stats.attackCoolDown)
            return actionAndCD
        if action in [ActionType.FLOOR_DOWN, ActionType.FLOOR_UP]:
            actionAndCD = (action, 0)
            return actionAndCD
        actionAndCD = (action, 0)
        return actionAndCD
