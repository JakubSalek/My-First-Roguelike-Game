import random
from enum import Enum
from GUI import GraphicElement


class TileType(Enum):
    WALL = 1
    FLOOR = 2
    STAIRS = 3
    DOOR_OPEN = 4
    DOOR_CLOSED = 5
    DOOR_KEY = 6
    EMPTY = 7


class Tile:
    items = []
    creature = None
    tileType = TileType.EMPTY

    def canPass(self):
        if self.tileType in [TileType.FLOOR, TileType.EMPTY, TileType.DOOR_OPEN, TileType.STAIRS] \
                and self.creature is None:
            return True
        else:
            return False


class DungeonMap:
    tileMap = [[Tile() for i in range(100)] for j in range(100)]

    def __init__(self):
        for i in range(40):
            for j in range(23):
                temp = random.randint(0, 3)
                if temp in (0, 1, 2):
                    self.tileMap[i][j].tileType = TileType.FLOOR
                    GraphicElement().initFloor(i, j)
                elif temp == 3:
                    self.tileMap[i][j].tileType = TileType.WALL
                    GraphicElement().initWall(i, j)
