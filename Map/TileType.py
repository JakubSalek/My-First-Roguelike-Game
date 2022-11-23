from enum import Enum


class TileType(Enum):
    WALL = 1
    FLOOR = 2
    STAIRS = 3
    DOOR_OPEN = 4
    DOOR_CLOSED = 5
    DOOR_KEY_LOCKED = 6
    EMPTY = 7
