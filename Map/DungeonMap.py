import random

import SETTINGS
from Creatures.ActorType import ActorType
from Map.Tile import Tile
from Map.TileType import TileType


class DungeonMap:
    tileMap = []

    def __init__(self):
        self.tileMap = [[Tile(i, j) for i in range(SETTINGS.MAP_SIZE_X_AND_Y)] for j in
                        range(SETTINGS.MAP_SIZE_X_AND_Y)]
        for i in range(SETTINGS.MAP_SIZE_X_AND_Y - 23):
            for j in range(SETTINGS.MAP_SIZE_X_AND_Y - 41):
                temp = random.randint(0, 3)
                if temp in (0, 1, 2):
                    self.tileMap[i][j].tileType = TileType.FLOOR
                elif temp == 3:
                    self.tileMap[i][j].tileType = TileType.WALL
        self.tileMap[0][0].tileType = TileType.STAIR_DOWN
        self.tileMap[5][0].tileType = TileType.STAIRS_UP
