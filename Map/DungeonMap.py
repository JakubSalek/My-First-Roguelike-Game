import random
from Map.Tile import Tile


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
