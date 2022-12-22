import random

import SETTINGS
from Map.Tile import Tile
from Map.TileType import TileType


class DungeonMap:
    tileMap = []

    def __init__(self):
        self.tileMap = [[Tile(i, j) for i in range(SETTINGS.MAP_SIZE_X_AND_Y)] for j in
                        range(SETTINGS.MAP_SIZE_X_AND_Y)]

    def generateMap(self, currentLevel):
        for i in range(SETTINGS.MAP_SIZE_X_AND_Y - SETTINGS.TILES_IN_COL):
            for j in range(SETTINGS.MAP_SIZE_X_AND_Y - SETTINGS.TILES_IN_ROW):
                temp = random.randint(0, 5)
                if temp in (0, 1, 2, 3, 4):
                    self.tileMap[i][j].tileType = TileType.FLOOR
                elif temp == 5:
                    self.tileMap[i][j].tileType = TileType.WALL
        self.tileMap[0][0].tileType = TileType.STAIR_DOWN
        self.tileMap[5][0].tileType = TileType.STAIRS_UP

    def populateMap(self, currentLevel):
        pass
