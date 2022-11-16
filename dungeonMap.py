from enum import Enum


class Tile_Type(Enum):
    EMPTY = 1
    WALL = 2
    FLOOR = 3
    STAIRS = 4
    DOOR_OPEN = 5
    DOOR_CLOSED = 6
    DOOR_KEY = 7
    VOID = 8


class Tile:
    items = []
    enemy = None
    type = Tile_Type.EMPTY

    def can_pass(self):
        # funkcja
        pass


class dungeonMap:
    def __init__(self, screenSizeX, screenSizeY):
        self.tileSizeX = int(screenSizeX/64)
        self.tileSizeY = int(screenSizeY/36)
    tilesList = []
