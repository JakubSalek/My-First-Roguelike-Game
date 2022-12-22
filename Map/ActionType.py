from enum import Enum


class ActionType(Enum):
    FLOOR_DOWN = 0
    FLOOR_UP = 1
    MOVE = 2
    ATTACK_MONSTER = 3
    CANT_MOVE = 4
    ATTACK_PLAYER = 5
    DOOR_LOCKED = 6
    SOMEONE_IS_DEAD = 7
    PLAYER_IS_DEAD = 8
