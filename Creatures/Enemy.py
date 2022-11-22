import random
from enum import Enum

from Creatures.Actor import Actor
from GUI import GraphicElement


class EnemyType(Enum):
    STUDENT = 1
    TEACHER = 2
    RAT = 3


class Enemy(Actor):
    def __init__(self):
        self.name = "Rat"
        self.description = "It stinks"
        self.stats.initRat()
        self.positionX = random.randint(10, 20)
        self.positionY = random.randint(5, 15)
        self.graphic = GraphicElement().initRat()

    def enemyMovement(self):
        self.inAction = True
        while self.inAction:
            self.move(random.randint(-1, 1), random.randint(-1, 1))
        return self.stats.getMoveCD()
