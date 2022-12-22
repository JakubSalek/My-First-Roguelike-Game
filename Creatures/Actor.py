from Creatures.ActorType import ActorType
from Creatures.ActorStatistics import Statistics
from Map.ActionType import ActionType
from Map.DungeonMap import DungeonMap


class Actor:
    name = ""
    description = ""
    positionX = int
    positionY = int
    stats = Statistics
    inAction = False
    isDead = False
    dungeonMap = DungeonMap.tileMap
    actorType = ActorType.EMPTY

    def setDungeonMap(self, dungeonMap):
        self.dungeonMap = dungeonMap
        self.dungeonMap[self.positionY][self.positionX].actor = self

    def getPosition(self):
        pos = (self.positionX, self.positionY)
        return pos

    def setPosition(self, x, y):
        self.positionX = x
        self.positionY = y

    def move(self, offSetX=0, offSetY=0):
        action = self.dungeonMap[self.positionY + offSetY][self.positionX + offSetX].canPass(self)
        # Jeśli pole, na którym chce stanąć, jest wolne albo są na nim schody w górę lub w dół
        if action in [ActionType.MOVE, ActionType.FLOOR_UP, ActionType.FLOOR_DOWN]:
            self.dungeonMap[self.positionY][self.positionX].setCreature(None)
            self.positionX += offSetX
            self.positionY += offSetY
            if action == ActionType.MOVE:
                self.dungeonMap[self.positionY][self.positionX].setCreature(self)
        elif action == ActionType.ATTACK_MONSTER:
            attackedCreature = self.dungeonMap[self.positionY + offSetY][self.positionX + offSetX].getCreature()
            attackedCreature.isDead = attackedCreature.stats.changeCurrentHP(-self.stats.currentStrength)
            if attackedCreature.isDead:
                self.dungeonMap[attackedCreature.positionY][attackedCreature.positionX].setCreature(None)
        elif action == ActionType.ATTACK_PLAYER:
            attackedCreature = self.dungeonMap[self.positionY + offSetY][self.positionX + offSetX].getCreature()
            attackedCreature.isDead = attackedCreature.stats.changeCurrentHP(-self.stats.currentStrength)
        self.inAction = False
        return action
