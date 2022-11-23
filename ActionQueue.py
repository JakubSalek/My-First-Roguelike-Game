from queue import PriorityQueue


class ActionQueue:

    def __init__(self, length, creatures):
        self.gameQueue = PriorityQueue()
        for i in range(length):
            self.gameQueue.put((0, i))
            i += 1
        self.currentTurn = 0
        self.creatures = creatures

    def nextTurn(self):
        turn, index = self.gameQueue.get()
        self.currentTurn = turn
        if index == 0:
            cooldown = self.creatures[index].playerMovement()
            self.gameQueue.put(((self.currentTurn + cooldown), index))
        else:
            cooldown = self.creatures[index].enemyMovement()
            self.gameQueue.put(((self.currentTurn + cooldown), index))