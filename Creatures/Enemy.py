import random

from Creatures.ActorStatistics import Statistics
from Creatures.ActorType import ActorType
from Creatures.Actor import Actor
from Map.ActionType import ActionType


class Enemy(Actor):
    items = []

    def __init__(self, actorType):
        if actorType is ActorType.RAT:
            self.initRat()
        elif actorType is ActorType.STUDENT:
            self.initStudent()
        elif actorType is ActorType.BUG:
            self.initBug()

    def initRat(self):
        self.name = "Rat"
        self.description = "It stinks"
        self.actorType = ActorType.RAT
        self.stats = Statistics(self.actorType)

    def initStudent(self):
        self.name = "Student"
        self.description = "He asks if you want to share your code"
        self.actorType = ActorType.STUDENT
        self.stats = Statistics(self.actorType)

    def initBug(self):
        self.name = "Bug"
        self.description = "How i hate them"
        self.actorType = ActorType.BUG
        self.stats = Statistics(self.actorType)

    def enemyMovement(self):
        actionType = ActionType.MOVE
        self.inAction = True
        for i in range(self.positionX-1, self.positionX+2):
            for j in range(self.positionY-1, self.positionY+2):
                if self.dungeonMap[j][i].actor is not None and \
                        self.dungeonMap[j][i].actor.actorType is ActorType.PLAYER:
                    actionType = self.move(i - self.positionX, j - self.positionY)
        while self.inAction:
            randX = random.randint(-1, 1)
            if not randX == 0:
                actionType = self.move(randX, 0)
            else:
                randY = 0
                while randY == 0:
                    randY = random.randint(-1, 1)
                actionType = self.move(0, randY)
        if actionType is ActionType.MOVE:
            return self.stats.movementCoolDown
        else:
            return self.stats.attackCoolDown
