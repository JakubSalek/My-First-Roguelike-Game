from Creatures.ActorType import ActorType
from Map.ActionType import ActionType
from Map.TileType import TileType


class Tile:
    def __init__(self, i, j):
        self.posX = i
        self.posY = j
        self.items = []
        self.actor = None
        self.tileType = TileType.EMPTY
        self.flooded = False

    def getPosition(self):
        pos = (self.posX, self.posY)
        return pos

    def setCreature(self, creature):
        self.actor = creature

    def getCreature(self):
        return self.actor

    # Sprawdzenie, czy gracz może przejść i w co wchodzi
    def canPass(self, attacker):
        if self.tileType in [TileType.FLOOR, TileType.DOOR_OPEN, TileType.DOOR_CLOSED] \
                and self.actor is None:
            if self.tileType is TileType.DOOR_CLOSED:
                self.tileType = TileType.DOOR_OPEN
            return ActionType.MOVE
        elif self.actor is not None:
            if self.actor.actorType is ActorType.PLAYER and attacker.actorType is not ActorType.PLAYER:
                return ActionType.ATTACK_PLAYER
            elif self.actor.actorType is not ActorType.PLAYER and attacker.actorType is ActorType.PLAYER:
                return ActionType.ATTACK_MONSTER
        elif self.tileType is TileType.STAIRS_UP:
            if attacker.actorType is ActorType.PLAYER:
                return ActionType.FLOOR_UP
            else:
                return ActionType.MOVE
        elif self.tileType is TileType.STAIR_DOWN:
            if attacker.actorType is ActorType.PLAYER:
                return ActionType.FLOOR_DOWN
            else:
                return ActionType.MOVE
        elif self.tileType is TileType.DOOR_KEY_LOCKED:
            return ActionType.DOOR_LOCKED
        else:
            return ActionType.CANT_MOVE
