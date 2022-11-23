from GUI import GraphicElement
from ActionQueue import ActionQueue
from Creatures.PlayerCharacter import Hero
from dungeonMap import DungeonMap


class GameEngine:

    def __init__(self, screen, clock):
        self.clock = clock
        self.screen = screen
        self.currentLevel = 0
        self.maxLevel = 0
        self.enemiesArr = [[] for j in range(15)]
        self.enemiesArr[0].append(Hero())
        self.mapsArr = []
        self.mapsArr.append(DungeonMap())
        self.queuesArr = []
        self.queuesArr.append(ActionQueue(len(self.enemiesArr[self.currentLevel]), self.enemiesArr[self.currentLevel]))
        self.GUI = GraphicElement()
        self.maxTurn = 0

    def getGameLevel(self):
        return self.currentLevel

    def startGame(self):
        self.enemiesArr[0][0].setDungeonMap(self.mapsArr[self.currentLevel].tileMap)
        while True:
            self.GUI.printMap(self.screen, self.mapsArr[self.currentLevel].tileMap,
                              self.enemiesArr[self.currentLevel])
            self.queuesArr[self.currentLevel].nextTurn()
            self.clock.tick(60)
