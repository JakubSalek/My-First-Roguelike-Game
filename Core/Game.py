from Creatures.Actor import Actor
from Creatures.ActorType import ActorType
from Creatures.Enemy import Enemy
from Graphics.GUI import GraphicElement
from ActionQueue import ActionQueue
from Creatures.Player import Hero
from Map.ActionType import ActionType
from Map.DungeonMap import DungeonMap


class GameEngine:

    # Inicjacja pierwszego poziomu i głównych zmiennych silnika
    def __init__(self, screen, clock):
        self.clock = clock
        self.screen = screen
        self.currentLevel = 0
        self.maxLevel = 0
        self.maxTurn = 0
        # Tablica obiektów map zawierających w sobie dwuwymiarowe tablice map
        self.mapsArr = [DungeonMap()]
        self.mapsArr[0].generateMap(self.currentLevel)
        self.player = Hero()
        self.player.setDungeonMap(self.mapsArr[self.currentLevel].tileMap)
        # Dwuwymiarowa tablica potworów
        self.enemiesArr = [[Actor() for j in range(1)] for i in range(15)]
        self.enemiesArr[0][0] = self.player
        self.generateEnemies()
        # Tablica kolejek na każde piętro
        self.queuesArr = []
        self.queuesArr.append(ActionQueue(self.enemiesArr[self.currentLevel], self.maxTurn))
        self.GUI = GraphicElement()

    def getGameLevel(self):
        return self.currentLevel

    # Główna pętla gry
    def startGame(self):
        while True:
            self.GUI.printMap(self.screen, self.mapsArr[self.currentLevel].tileMap,
                              self.enemiesArr[self.currentLevel])
            action = self.queuesArr[self.currentLevel].nextTurn(self.enemiesArr[self.currentLevel])
            if action == ActionType.FLOOR_UP:
                self.decrementLevel()
            if action == ActionType.FLOOR_DOWN:
                self.incrementLevel()

    # Przemieszczenie gracza na inny poziom lochu
    def addPlayerToLevel(self):
        self.enemiesArr[self.currentLevel].insert(0, self.player)
        self.player.setDungeonMap(self.mapsArr[self.currentLevel].tileMap)
        x, y = self.player.getPosition()
        self.mapsArr[self.currentLevel].tileMap[y][x].actorType = ActorType.PLAYER

    # Zmiana poziomu lochu
    def changeLevel(self, i):
        self.maxTurn = self.queuesArr[self.currentLevel].getTurn()
        self.enemiesArr[self.currentLevel].pop(0)
        self.currentLevel += i

    # Zmiana poziomu w dół
    def incrementLevel(self):
        # Maksymalne piętro 14 (15 pięter licząc od 0)
        if self.currentLevel != 14:
            self.changeLevel(1)
            # Jeśli poziom jeszcze nie istnieje to go generujemy
            if self.currentLevel > self.maxLevel:
                self.generateNextLevel()
            # Jeśli już istnieje to przemieszczamy tylko gracza na kolejny poziom
            else:
                self.addPlayerToLevel()

    # Zmiana poziomu w górę
    def decrementLevel(self):
        # Minimalne piętro 0, poprzednie piętro zawsze będzie istniało
        if self.currentLevel != 0:
            self.changeLevel(-1)
            self.queuesArr[self.currentLevel].playUntilTurn(self.maxTurn, self.enemiesArr[self.currentLevel])
            self.addPlayerToLevel()
            self.enemiesArr[self.currentLevel][0].setDungeonMap(self.mapsArr[self.currentLevel].tileMap)

    # Generowanie przeciwników na poziomie lochu
    def generateEnemies(self):
        for i in range(5):
            self.enemiesArr[self.currentLevel].append(Enemy(ActorType.RAT))
        for enemy in self.enemiesArr[self.currentLevel]:
            enemy.setDungeonMap(self.mapsArr[self.currentLevel].tileMap)

    # Generowanie nowego poziomu lochu
    def generateNextLevel(self):
        self.maxLevel += 1
        self.enemiesArr[self.currentLevel][0] = self.player
        self.mapsArr.append(DungeonMap())
        self.mapsArr[self.currentLevel].generateMap(self.currentLevel)
        self.player.setDungeonMap(self.mapsArr[self.currentLevel].tileMap)
        x, y = self.player.getPosition()
        self.mapsArr[self.currentLevel].tileMap[y][x].actorType = ActorType.PLAYER
        self.queuesArr.append(ActionQueue(self.enemiesArr[self.currentLevel], self.maxTurn))
