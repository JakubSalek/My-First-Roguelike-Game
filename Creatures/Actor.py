import random

import pygame

from Creatures.ActorType import ActorType
from Creatures.ActorStatistics import Statistics
from Map.ActionType import ActionType
from Map.DungeonMap import DungeonMap
from Map.TileType import TileType


class Actor:
    name = ""
    description = ""
    positionX = int
    positionY = int
    stats = Statistics
    inAction = False
    isDead = False
    dungeonMap = DungeonMap.tileMap
    actorType = ActorType.EMPTY

    def setDungeonMap(self, dungeonMap):
        self.dungeonMap = dungeonMap
        while True and self.actorType is not ActorType.PLAYER:
            posX = random.randint(21, 79)
            posY = random.randint(21, 79)
            if dungeonMap[posY][posX].actor is None and dungeonMap[posY][posX].tileType is TileType.FLOOR:
                self.positionX = posX
                self.positionY = posY
                break
        self.dungeonMap[self.positionY][self.positionX].actor = self

    def getPosition(self):
        pos = (self.positionX, self.positionY)
        return pos

    def setPosition(self, x, y):
        self.positionX = x
        self.positionY = y

    def fight(self, defender):
        # Sprawdzamy, czy atak trafi, a jeśli trafi to czy krytycznie
        attackMultiply = 0
        attackerRoll = random.randint(0, self.stats.currentAgility)
        defenderRoll = random.randint(0, defender.stats.currentAgility)
        if attackerRoll > 2 * defenderRoll:
            attackMultiply = 1.5
        elif attackerRoll > defenderRoll:
            attackMultiply = 1
        else:
            attackMultiply = 0
        # Obliczamy zadane obrażenia i odejmujemy je od obrońcy (Tu trzeba dodać jeszcze przedmioty)
        attackerDamage = random.randint(1, self.stats.currentStrength) * attackMultiply
        # defenderDefence =
        damageDealt = attackerDamage
        defender.isDead = defender.stats.changeCurrentHP(-damageDealt)
        if defender.isDead:
            if defender.actorType is ActorType.PLAYER:
                print("Game Over!")
                pygame.quit()
                exit()
            self.stats.addXP(defender.stats.expOnDeath)

    def move(self, offSetX=0, offSetY=0):
        action = self.dungeonMap[self.positionY + offSetY][self.positionX + offSetX].canPass(self)
        # Jeśli pole, na którym chce stanąć, jest wolne albo są na nim schody w górę lub w dół
        if action in [ActionType.MOVE, ActionType.FLOOR_UP, ActionType.FLOOR_DOWN]:
            self.dungeonMap[self.positionY][self.positionX].setCreature(None)
            self.positionX += offSetX
            self.positionY += offSetY
            if action == ActionType.MOVE:
                self.dungeonMap[self.positionY][self.positionX].setCreature(self)
        elif action == ActionType.ATTACK_MONSTER:
            attackedCreature = self.dungeonMap[self.positionY + offSetY][self.positionX + offSetX].getCreature()
            self.fight(attackedCreature)
            if attackedCreature.isDead:
                self.dungeonMap[attackedCreature.positionY][attackedCreature.positionX].setCreature(None)
        elif action == ActionType.ATTACK_PLAYER:
            attackedCreature = self.dungeonMap[self.positionY + offSetY][self.positionX + offSetX].getCreature()
            self.fight(attackedCreature)
        self.inAction = False
        return action
