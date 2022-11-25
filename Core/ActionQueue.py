from queue import PriorityQueue


class ActionQueue:

    def __init__(self, creatures, turn):
        self.gameQueue = PriorityQueue()
        for i in range(len(creatures)):
            self.gameQueue.put((0, i))
        self.currentTurn = turn

    def getTurn(self):
        return self.currentTurn

    # Wykonaj kolejną turę
    def nextTurn(self, creatures):
        turn, index = self.gameQueue.get()
        self.currentTurn = turn
        if index == 0:
            action, cooldown = creatures[index].playerMovement()
            self.gameQueue.put(((self.currentTurn + cooldown), index))
            return action
        else:
            cooldown = creatures[index].enemyMovement()
            self.gameQueue.put(((self.currentTurn + cooldown), index))
            return 100

    # Symuluj ruchy po powrocie na poziom wcześniej
    def playUntilTurn(self, turn, creatures):
        if creatures:
            while self.currentTurn < turn:
                turn, index = self.gameQueue.get()
                self.currentTurn = turn
                cooldown = creatures[index-1].enemyMovement()
                self.gameQueue.put((self.currentTurn + cooldown), index)
