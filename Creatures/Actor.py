from Creatures.ActorType import ActorType
from Creatures.Statistics import Statistics
from Map.DungeonMap import DungeonMap


class Actor:
    name = ""
    description = ""
    positionX = int
    positionY = int
    items = []
    stats = Statistics()
    inAction = False
    dungeonMap = DungeonMap.tileMap
    actorType = ActorType.EMPTY

    def setDungeonMap(self, dungeonMap):
        self.dungeonMap = dungeonMap
        self.dungeonMap[self.positionY][self.positionX].actorType = self.actorType

    def getPosition(self):
        pos = (self.positionX, self.positionY)
        return pos

    def setPosition(self, x, y):
        self.positionX = x
        self.positionY = y

    def move(self, offSetX=0, offSetY=0):
        action = self.dungeonMap[self.positionY + offSetY][self.positionX + offSetX].canPass()
        if action in [2, -1, 1]:
            self.dungeonMap[self.positionY][self.positionX].setCreature(ActorType.EMPTY)
            self.positionX += offSetX
            self.positionY += offSetY
            if action == 2:
                self.dungeonMap[self.positionY][self.positionX].setCreature(self.actorType)
            self.inAction = False
        return action
