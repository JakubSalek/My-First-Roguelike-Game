import pygame

import SETTINGS

graphicElementsList = []


class GraphicElement:
    surface = None
    positionX = int
    positionY = int

    def getSurface(self):
        return self.surface

    def getPosition(self):
        pos = (self.positionX, self.positionY)
        return pos

    def moveGraphic(self, offsetX=0, offsetY=0):
        self.positionX += offsetX*SETTINGS.tileWidth
        self.positionY += offsetY*SETTINGS.tileHeight

    def setPosition(self, positionX, positionY):
        self.positionX = positionX * SETTINGS.tileWidth
        self.positionY = positionY * SETTINGS.tileHeight

    def initPlayer(self, positionX, positionY):
        self.setPosition(positionX, positionY)
        self.surface = pygame.image.load("Assets/hero.png").convert_alpha()
        graphicElementsList.append(self)
        return self

    def initWall(self, positionX, positionY):
        self.setPosition(positionX, positionY)
        self.surface = pygame.image.load("Assets/wall.png")
        graphicElementsList.append(self)

    def initFloor(self, positionX, positionY):
        self.setPosition(positionX, positionY)
        self.surface = pygame.image.load("Assets/floor.png")
        graphicElementsList.append(self)
