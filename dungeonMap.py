import random
from enum import Enum


class TileType(Enum):
    WALL = 1
    FLOOR = 2
    STAIRS = 3
    DOOR_OPEN = 4
    DOOR_CLOSED = 5
    DOOR_KEY_LOCKED = 6
    EMPTY = 7


class Tile:
    def __init__(self, i, j):
        self.posX = i
        self.posY = j
        self.items = []
        self.creature = None
        self.tileType = TileType.EMPTY

    def getPosition(self):
        pos = (self.posX, self.posY)
        return pos

    def setCreature(self, creature):
        self.creature = creature

    # Tutaj trzeba pomyśleć co jak będzie chciało wejść we wroga lub drzwi np
    def canPass(self):
        if self.tileType in [TileType.FLOOR, TileType.DOOR_OPEN, TileType.STAIRS] \
                and self.creature is None:
            return True
        else:
            return False

    def initFloor(self):
        self.tileType = TileType.FLOOR

    def initWall(self):
        self.tileType = TileType.WALL


class DungeonMap:
    tileMap = [[Tile(i, j) for i in range(100)] for j in range(100)]

    def __init__(self):
        for i in range(80):
            for j in range(80):
                temp = random.randint(0, 3)
                if temp in (0, 1, 2):
                    self.tileMap[i][j].initFloor()
                elif temp == 3:
                    self.tileMap[i][j].initWall()
