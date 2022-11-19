import GUI
from Statistics import Statistics
from dungeonMap import DungeonMap


class Actor:
    name = ""
    description = ""
    positionX = int
    positionY = int
    items = []
    actorStats = Statistics()
    graphic = None

    def setPosition(self, x, y):
        self.positionX = x
        self.positionY = y

    def move(self, direction):
        if direction == "DOWN":
            if DungeonMap.tileMap[self.positionX][self.positionY+1].canPass():
                self.graphic.moveGraphic(offsetY=1)
                self.positionY += 1
                return True
            else:
                return False
        if direction == "UP":
            if DungeonMap.tileMap[self.positionX][self.positionY-1].canPass():
                self.graphic.moveGraphic(offsetY=-1)
                self.positionY -= 1
                return True
            else:
                return False
        if direction == "LEFT":
            if DungeonMap.tileMap[self.positionX-1][self.positionY].canPass():
                self.graphic.moveGraphic(offsetX=-1)
                self.positionX -= 1
                return True
            else:
                return False
        if direction == "RIGHT":
            if DungeonMap.tileMap[self.positionX+1][self.positionY].canPass():
                self.graphic.moveGraphic(offsetX=+1)
                self.positionX += 1
                return True
            else:
                return False
