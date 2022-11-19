class Statistics:
    currentHealth = int
    maxHealth = int
    attackCoolDown = float
    strength = int
    agility = int

    def initPlayer(self):
        self.strength = 10
        self.agility = 10
        self.maxHealth = 20
        self.currentHealth = 20
        self.attackCoolDown = 3.0
