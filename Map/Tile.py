from Creatures.ActorType import ActorType
from Map.TileType import TileType


class Tile:
    def __init__(self, i, j):
        self.posX = i
        self.posY = j
        self.items = []
        self.actorType = ActorType.EMPTY
        self.tileType = TileType.EMPTY

    def getPosition(self):
        pos = (self.posX, self.posY)
        return pos

    def setCreature(self, creature):
        self.actorType = creature

    def getCreature(self):
        return self.actorType

    # Sprawdzenie, czy gracz może przejść i w co wchodzi
    def canPass(self):
        if self.tileType in [TileType.FLOOR, TileType.DOOR_OPEN, TileType.DOOR_CLOSED] \
                and self.actorType is ActorType.EMPTY:
            if self.tileType is TileType.DOOR_CLOSED:
                self.tileType = TileType.DOOR_OPEN
            # 2 - może przejść
            return 2
        elif self.tileType in [TileType.FLOOR, TileType.DOOR_OPEN] and self.actorType is not ActorType.EMPTY:
            # 3 - atakuje wroga
            return 3
        elif self.tileType is TileType.STAIRS_UP:
            # 1 - poziom w górę
            return 1
        elif self.tileType is TileType.STAIR_DOWN:
            # -1 - poziom w dół
            return -1
        elif self.tileType is TileType.DOOR_KEY_LOCKED:
            # Drzwi zamknięte na klucz
            return 4
        else:
            # Nie może przejść
            return 0
