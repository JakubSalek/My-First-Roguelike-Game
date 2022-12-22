from Creatures.ActorType import ActorType


class Statistics:
    baseStrength = int
    currentStrength = int
    baseAgility = int
    currentAgility = int
    baseDefense = int
    currentDefense = int
    maxHealth = int
    currentHealth = int
    attackCoolDown = float
    movementCoolDown = float
    currentExperience = int
    maxExperience = int
    expOnDeath = int

    def __init__(self, actorType):
        if actorType is ActorType.PLAYER:
            self.baseStrength = 10
            self.currentStrength = self.baseStrength
            self.baseAgility = 10
            self.currentAgility = self.baseAgility
            self.maxHealth = 20
            self.currentHealth = self.maxHealth
            self.currentExperience = 0
            self.maxExperience = 10
            self.attackCoolDown = 3.0
            self.movementCoolDown = 1.0
        elif actorType is ActorType.RAT:
            self.baseStrength = 2
            self.currentStrength = self.baseStrength
            self.baseAgility = 3
            self.currentAgility = self.baseAgility
            self.maxHealth = 10
            self.currentHealth = self.maxHealth
            self.attackCoolDown = 3.0
            self.movementCoolDown = 3.0
            self.expOnDeath = 1

    def changeCurrentHP(self, health):
        self.currentHealth += health
        if health < 0:
            return True
        else:
            return False

    def addXP(self, XP):
        self.currentExperience += XP
        if self.currentExperience >= self.maxExperience:
            self.levelUP()

    # Zaimplementować
    def levelUP(self):
        pass
