from enum import Enum

from Entity import Entity, EntityTypes


class Tile_Type(Enum):
    WALL = 1
    FLOOR = 2
    STAIRS = 3
    DOOR_OPEN = 4
    DOOR_CLOSED = 5
    DOOR_KEY = 6
    EMPTY = 7


class Tile(Entity):
    def __init__(self):
        self.setType(EntityTypes.ENVIRONMENT)

    creature = None
    tileType = Tile_Type.EMPTY

    def can_pass(self):
        # funkcja
        if self.tileType in [Tile_Type.FLOOR, Tile_Type.EMPTY, Tile_Type.DOOR_OPEN, Tile_Type.STAIRS] \
                and self.creature is None:
            return True
        else:
            return False


class dungeonMap:
    tileMap = [[Tile for i in range(100)] for j in range(100)]
    for i in range(100):
        for j in range(100):
            tileMap[i][j].tileType = Tile_Type.FLOOR
    for i in range(10, 25):
        for j in range(5, 15):
            tileMap[i][j].tileType = Tile_Type.WALL
