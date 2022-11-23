import random
from EnemyType import EnemyType
from Creatures.Actor import Actor


class Enemy(Actor):
    def __init__(self):
        self.name = "Rat"
        self.description = "It stinks"
        self.enemyType = EnemyType.RAT
        self.stats.initRat()
        self.positionX = random.randint(10, 20)
        self.positionY = random.randint(5, 15)

    def enemyMovement(self):
        self.inAction = True
        while self.inAction:
            self.move(random.randint(-1, 1), random.randint(-1, 1))
        return self.stats.getMoveCD()
