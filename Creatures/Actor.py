from Statistics import Statistics


class Actor:
    name = ""
    description = ""
    positionX = int
    positionY = int
    items = []
    stats = Statistics()
    inAction = False
    dungeonMap = None

    def setDungeonMap(self, dungeonMap):
        self.dungeonMap = dungeonMap

    def getGraphic(self):
        return self.graphic

    def getPosition(self):
        pos = (self.positionX, self.positionY)
        return pos

    def setPosition(self, x, y):
        self.positionX = x
        self.positionY = y

    def move(self, offSetX=0, offSetY=0):
        if self.dungeonMap[self.positionY+offSetY][self.positionX+offSetX].canPass():
            self.dungeonMap[self.positionY][self.positionX].setCreature(None)
            self.positionX += offSetX
            self.positionY += offSetY
            self.dungeonMap[self.positionY][self.positionX].setCreature(self)
            self.inAction = False
