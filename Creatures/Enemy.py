import random
from Creatures.ActorType import ActorType
from Creatures.Actor import Actor


class Enemy(Actor):
    def __init__(self):
        self.name = "Rat"
        self.description = "It stinks"
        self.enemyType = ActorType.RAT
        self.stats.initRat()
        self.positionX = 5
        self.positionY = 5

    def enemyMovement(self):
        self.inAction = True
        while self.inAction:
            self.move(random.randint(-1, 1), random.randint(-1, 1))
        return self.stats.getMoveCD()
