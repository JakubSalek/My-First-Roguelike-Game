import queue
import random

import SETTINGS
from Map.Tile import Tile
from Map.TileType import TileType


def floodFill(tile, dungMap):
    canGoDown = False
    q = queue.Queue()
    q.put(tile)
    while not q.empty():
        n = q.get()
        if not n.flooded and n.tileType is not TileType.WALL:
            n.flooded = True
            if n.tileType is TileType.STAIR_DOWN:
                canGoDown = True
            q.put(dungMap[n.posY-1][n.posX])
            q.put(dungMap[n.posY+1][n.posX])
            q.put(dungMap[n.posY][n.posX+1])
            q.put(dungMap[n.posY][n.posX-1])
    return canGoDown


class DungeonMap:
    tileMap = []
    stairsDownPos = None
    stairsUpPos = None

    def __init__(self):
        self.tileMap = [[Tile(i, j) for i in range(SETTINGS.MAP_SIZE_X_AND_Y)] for j in
                        range(SETTINGS.MAP_SIZE_X_AND_Y)]

    def generateMap(self, currentLevel, stairsPos):
        for i in range(20, 81):
            for j in range(20, 81):
                self.tileMap[i][j].tileType = TileType.WALL

        self.stairsUpPos = stairsPos
        y, x = self.stairsUpPos
        self.tileMap[y][x].tileType = TileType.STAIRS_UP

        stairsDownOnPlace = False
        while not stairsDownOnPlace:
            stairDownX = random.randint(21, 79)
            stairDownY = random.randint(21, 79)
            if self.tileMap[stairDownY][stairDownX].tileType is TileType.WALL:
                self.tileMap[stairDownY][stairDownX].tileType = TileType.STAIR_DOWN
                self.stairsDownPos = (stairDownY, stairDownX)
                stairsDownOnPlace = True

        wayToStairs = False
        while not wayToStairs:
            filled = False
            while not filled:
                wallX = random.randint(21, 79)
                wallY = random.randint(21, 79)
                if self.tileMap[wallY][wallX].tileType is TileType.WALL:
                    self.tileMap[wallY][wallX].tileType = TileType.FLOOR
                    filled = True
                    for i in range(21, 80):
                        for j in range(21, 80):
                            self.tileMap[i][j].flooded = False
                    wayToStairs = floodFill(self.tileMap[y][x], self.tileMap)

    def populateMap(self, currentLevel):
        pass
