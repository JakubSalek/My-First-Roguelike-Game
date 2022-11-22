import pygame
import SETTINGS


class GraphicElement:
    surface = None
    positionX = int
    positionY = int

    def getSurface(self):
        return self.surface

    def getPosition(self):
        pos = (self.positionX, self.positionY)
        return pos

    def setPosition(self, positionX, positionY):
        self.positionX = positionX * SETTINGS.TILE_WIDTH
        self.positionY = positionY * SETTINGS.TILE_HEIGHT

    def initPlayer(self):
        self.surface = pygame.image.load("Assets/hero.png").convert_alpha()
        return self

    def initRat(self):
        self.surface = pygame.image.load("Assets/rat.png")
        return self

    def initWall(self):
        self.surface = pygame.image.load("Assets/wall.png")
        return self

    def initFloor(self):
        self.surface = pygame.image.load("Assets/floor.png")
        return self

    def initBackGround(self):
        self.setPosition(0, 0)
        self.surface = pygame.Surface((SETTINGS.SCREEN_WIDTH, SETTINGS.SCREEN_HEIGHT))
        self.surface.fill("Black")
        return self

    def initBlackSquare(self, positionX, positionY):
        self.setPosition(positionX, positionY)
        self.surface = pygame.Surface(SETTINGS.TILE_SIZE)
        self.surface.fill("Black")
        return self


class GraphicalMapRepresentation:
    background = GraphicElement().initBackGround()

    def printMap(self, screen, dungeonMap, creatures, heroPos):
        screen.blit(self.background.getSurface(), self.background.getPosition())
        heroPosX, heroPosY = heroPos
        for i in range(22):
            for j in range(40):
                screen.blit(dungeonMap[heroPosY-11+i][heroPosX-20+j].graphic.getSurface(),
                            (j*SETTINGS.TILE_WIDTH, i*SETTINGS.TILE_HEIGHT))
        counter = 0
        for creature in creatures:
            if counter == 0:
                screen.blit(creature.graphic.getSurface(),
                            (20*SETTINGS.TILE_WIDTH, 11*SETTINGS.TILE_HEIGHT))
                counter += 1
            else:
                creaturePosX, creaturePosY = creature.getPosition()
                screen.blit(creature.graphic.getSurface(),
                            (creaturePosX*SETTINGS.TILE_WIDTH, creaturePosY*SETTINGS.TILE_HEIGHT))

        pygame.display.update()
