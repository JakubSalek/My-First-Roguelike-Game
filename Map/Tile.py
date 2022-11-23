from Map.TileType import TileType


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

