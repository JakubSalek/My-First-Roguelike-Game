from Creatures.Actor import Actor
from Creatures.ActorType import ActorType
from Creatures.Enemy import Enemy
from Graphics.GUI import GraphicElement
from ActionQueue import ActionQueue
from Creatures.PlayerCharacter import Hero
from Map.DungeonMap import DungeonMap


class GameEngine:

    def __init__(self, screen, clock):
        self.clock = clock
        self.screen = screen
        self.currentLevel = 0
        self.maxLevel = 0
        self.maxTurn = 0
        self.mapsArr = []
        self.mapsArr.append(DungeonMap())
        self.player = Hero()
        self.player.setDungeonMap(self.mapsArr[self.currentLevel].tileMap)
        self.enemiesArr = [[Actor() for j in range(1)] for i in range(15)]
        self.enemiesArr[0][0] = self.player
        # self.generateEnemies()
        self.queuesArr = []
        self.queuesArr.append(ActionQueue(self.enemiesArr[self.currentLevel], self.maxTurn))
        self.GUI = GraphicElement()

    def getGameLevel(self):
        return self.currentLevel

    def startGame(self):
        while True:
            self.GUI.printMap(self.screen, self.mapsArr[self.currentLevel].tileMap,
                              self.enemiesArr[self.currentLevel])
            action = self.queuesArr[self.currentLevel].nextTurn(self.enemiesArr[self.currentLevel])
            if action == 1:
                self.decrementLevel()
            if action == -1:
                self.incrementLevel()
            self.clock.tick(60)

    def addPlayerToLevel(self):
        self.enemiesArr[self.currentLevel].insert(0, self.player)
        self.player.setDungeonMap(self.mapsArr[self.currentLevel].tileMap)
        x, y = self.player.getPosition()
        self.mapsArr[self.currentLevel].tileMap[y][x].actorType = ActorType.PLAYER

    def changeLevel(self, i):
        self.maxTurn = self.queuesArr[self.currentLevel].getTurn()
        self.enemiesArr[self.currentLevel].pop(0)
        self.currentLevel += i

    # Zmiana poziomu w dół
    def incrementLevel(self):
        if self.currentLevel != 14:
            self.changeLevel(1)
            if self.currentLevel > self.maxLevel:
                self.generateNextLevel()
            else:
                self.addPlayerToLevel()

    # Zmiana poziomu w górę
    def decrementLevel(self):
        if self.currentLevel != 0:
            self.changeLevel(-1)
            self.queuesArr[self.currentLevel].playUntilTurn(self.maxTurn, self.enemiesArr[self.currentLevel])
            self.addPlayerToLevel()
            self.enemiesArr[self.currentLevel][0].setDungeonMap(self.mapsArr[self.currentLevel].tileMap)

    def generateEnemies(self):
        self.enemiesArr[self.currentLevel].append(Enemy())
        for enemy in self.enemiesArr[self.currentLevel]:
            enemy.dungeonMap.setDungeonMap(self.mapsArr[self.currentLevel].tileMap)

    # Generowanie poziomu
    def generateNextLevel(self):
        self.maxLevel += 1
        self.enemiesArr[self.currentLevel][0] = self.player
        self.mapsArr.append(DungeonMap())
        self.player.setDungeonMap(self.mapsArr[self.currentLevel].tileMap)
        x, y = self.player.getPosition()
        self.mapsArr[self.currentLevel].tileMap[y][x].actorType = ActorType.PLAYER
        self.queuesArr.append(ActionQueue(self.enemiesArr[self.currentLevel], self.maxTurn))
