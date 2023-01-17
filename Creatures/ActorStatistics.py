from Creatures.ActorType import ActorType


class Statistics:
    baseStrength = None
    currentStrength = None
    baseAgility = None
    currentAgility = None
    baseDefense = None
    currentDefense = None
    maxHealth = None
    currentHealth = None
    attackCoolDown = None
    movementCoolDown = None
    currentExperience = None
    maxExperience = None
    expOnDeath = None

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
            self.maxHealth = 100
            self.currentHealth = self.maxHealth
            self.attackCoolDown = 3.0
            self.movementCoolDown = 3.0
            self.expOnDeath = 5

    def changeCurrentHP(self, health):
        self.currentHealth += health
        if self.currentHealth < 0:
            return True
        else:
            return False

    def addXP(self, XP):
        self.currentExperience += XP
        if self.currentExperience >= self.maxExperience:
            self.levelUP()

    # Zaimplementować
    def levelUP(self):
        self.currentExperience = 0
        self.maxExperience *= 1.75
        self.baseStrength += 2
        self.currentStrength += 2
        self.baseAgility += 1
        self.currentAgility += 1
        self.maxHealth += 5
        self.currentHealth += 5
