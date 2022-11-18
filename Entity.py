from enum import Enum
import SETTINGS


class EntityTypes(Enum):
    CHARACTER = 1
    ENEMY = 2
    ENVIRONMENT = 3


class Entity:
    type = EntityTypes
    positionX = int
    positionY = int
    tileSizeX = SETTINGS.tileWidth
    tileSizeY = SETTINGS.tileHeight
    inventory = []

    def setType(self, entityType):
        self.type = entityType

    def setPosition(self, x, y):
        self.positionX = x
        self.positionY = y

    def move(self, direction):
        if direction == "DOWN":
            self.positionY += self.tileSizeY
        if direction == "UP":
            self.positionY -= self.tileSizeY
        if direction == "LEFT":
            self.positionX -= self.tileSizeX
        if direction == "RIGHT":
            self.positionX += self.tileSizeX
