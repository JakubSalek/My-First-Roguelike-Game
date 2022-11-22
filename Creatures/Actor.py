from Statistics import Statistics
from dungeonMap import DungeonMap


class Actor:
    name = ""
    description = ""
    positionX = int
    positionY = int
    items = []
    stats = Statistics()
    graphic = None
    inAction = False

    def getGraphic(self):
        return self.graphic

    def getPosition(self):
        pos = (self.positionX, self.positionY)
        return pos

    def setPosition(self, x, y):
        self.positionX = x
        self.positionY = y

    def move(self, offSetX=0, offSetY=0):
        if DungeonMap.tileMap[self.positionX+offSetX][self.positionY+offSetY].canPass():
            DungeonMap.tileMap[self.positionX][self.positionY].setCreature(None)
            self.positionX += offSetX
            self.positionY += offSetY
            DungeonMap.tileMap[self.positionX][self.positionY].setCreature(self)
            self.inAction = False
