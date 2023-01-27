import random

from Creatures.ActorStatistics import Statistics
from Creatures.ActorType import ActorType
from Creatures.Actor import Actor


class Enemy(Actor):
    items = []

    def __init__(self, actorType):
        if actorType is ActorType.RAT:
            self.initRat()

    def initRat(self):
        self.name = "Rat"
        self.description = "It stinks"
        self.actorType = ActorType.RAT
        self.stats = Statistics(self.actorType)
        self.positionX = random.randint(20, 80)
        self.positionY = random.randint(20, 80)

    def enemyMovement(self):
        self.inAction = True
        while self.inAction:
            self.move(random.randint(-1, 1), random.randint(-1, 1))
        return self.stats.movementCoolDown
