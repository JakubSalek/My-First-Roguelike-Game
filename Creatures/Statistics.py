class Statistics:
    currentHealth = int
    maxHealth = int
    currentExperience = int
    maxExperience = int
    attackCoolDown = float
    movementCoolDown = float
    strength = int
    agility = int

    def getCurrentHP(self):
        return self.currentHealth

    def setCurrentHP(self, health):
        self.currentHealth = health

    def getMaxHP(self):
        return self.maxHealth

    def addXP(self, XP):
        self.currentExperience += XP
        if self.currentExperience >= self.maxExperience:
            self.levelUP()

    def getStrength(self):
        return self.strength

    def getAttackCD(self):
        return self.attackCoolDown

    def getMoveCD(self):
        return self.movementCoolDown

    def initPlayer(self):
        self.strength = 10
        self.agility = 10
        self.maxHealth = 20
        self.currentHealth = 20
        self.currentExperience = 0
        self.maxExperience = 10
        self.attackCoolDown = 3.0
        self.movementCoolDown = 1.0

    # Zaimplementować
    def levelUP(self):
        pass

    # Dodać funkcje lvl-up, dodać funkcje zmieniającą zdrowie

    def initRat(self):
        self.strength = 10
        self.agility = 10
        self.maxHealth = 20
        self.currentHealth = 20
        self.currentExperience = 0
        self.maxExperience = 10
        self.attackCoolDown = 3.0
        self.movementCoolDown = 1.0